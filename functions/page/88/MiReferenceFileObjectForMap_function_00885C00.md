# MiReferenceFileObjectForMap

- RVA: `0x00885C00`–`0x00885C2E` (길이 `46` bytes)
- VA: `0x0000000140885C00`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068804`
- 디코드: `16`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00885C24` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)

### Direct callers
- [MiInsertInSystemSpace](../../text/3B/MiInsertInSystemSpace_function_003B2F5C.md) at `0x003B3196`
- [sub_00884EE1](Unknown_function_00884EE1.md) at `0x0088508F`
- [MiAllowImageMap](../8C/MiAllowImageMap_function_008C8B10.md) at `0x008C8BD8`
- [MiMapViewOfImageSection](../97/MiMapViewOfImageSection_function_0097E92C.md) at `0x0097EC36`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00885C24` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00885C00  40 53                           push rbx
00885C02  48 83 EC 20                     sub rsp, 0x20
00885C06  48 8B 59 28                     mov rbx, qword ptr [rcx + 0x28]
00885C0A  F6 C3 03                        test bl, 3
00885C0D  75 09                           jne 0x140885c18
00885C0F  33 C0                           xor eax, eax
00885C11  48 83 C4 20                     add rsp, 0x20
00885C15  5B                              pop rbx
00885C16  C3                              ret
00885C17  CC                              int3
00885C18  48 83 E3 FC                     and rbx, 0xfffffffffffffffc
00885C1C  BA 4D 6D 53 63                  mov edx, 0x63536d4d
00885C21  48 8B CB                        mov rcx, rbx
00885C24  E8 E7 AA 98 FF                  call 0x140210710
00885C29  48 8B C3                        mov rax, rbx
00885C2C  EB E3                           jmp 0x140885c11
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReferenceFileObjectForMap(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 40))) & (3)) != 0) goto loc_00885C18;
    result = 0;
loc_00885C11:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00885C18:
    v_rbx = (*(unsigned __int64 *)(a1 + 40)) & (-4);
    result = ObfReferenceObjectWithTag(v_rbx, (unsigned int)(0x63536D4DULL), a3, a4);
    goto loc_00885C11;
}
```

## 5. (Beta) C Style

```c
int64_t MiReferenceFileObjectForMap(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x28))) & (3)) != 0) goto loc_00885C18;
    result = 0;
loc_00885C11:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00885C18:
    local_rbx = (*(uint64_t *)(arg1 + 0x28)) & (-4);
    result = ObfReferenceObjectWithTag(local_rbx, (uint32_t)(0x63536D4DULL), a3, a4);
    goto loc_00885C11;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00885C00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00885C00[BB_00885C00]
  bb_00885C0F[BB_00885C0F]
  bb_00885C11[BB_00885C11]
  bb_00885C17[BB_00885C17]
  bb_00885C18[BB_00885C18]
  bb_00885C00 -->|branch| bb_00885C18
  bb_00885C00 -->|fallthrough| bb_00885C0F
  bb_00885C0F -->|flow| bb_00885C11
  bb_00885C17 -->|flow| bb_00885C18
  bb_00885C18 -->|branch| bb_00885C11
```
