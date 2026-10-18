# ExSizeOfRundownProtectionCacheAware

- RVA: `0x00ABF3A0`–`0x00ABF3CE` (길이 `46` bytes)
- VA: `0x0000000140ABF3A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005DAC8`
- 디코드: `15`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00ABF3B1` → [KeGetRecommendedSharedDataAlignment](../../text/49/KeGetRecommendedSharedDataAlignment_function_00494040.md) (function, `0x00494040`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00ABF3A6` → RVA `0x00FC6A80` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00ABF3B1` → [KeGetRecommendedSharedDataAlignment](../../text/49/KeGetRecommendedSharedDataAlignment_function_00494040.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ABF3A0  40 53                           push rbx
00ABF3A2  48 83 EC 20                     sub rsp, 0x20
00ABF3A6  8B 1D D4 76 50 00               mov ebx, dword ptr [rip + 0x5076d4]
00ABF3AC  83 FB 01                        cmp ebx, 1
00ABF3AF  76 16                           jbe 0x140abf3c7
00ABF3B1  E8 8A 4C 9D FF                  call 0x140494040
00ABF3B6  8D 4B 01                        lea ecx, [rbx + 1]
00ABF3B9  0F AF C1                        imul eax, ecx
00ABF3BC  48 83 C0 18                     add rax, 0x18
00ABF3C0  48 83 C4 20                     add rsp, 0x20
00ABF3C4  5B                              pop rbx
00ABF3C5  C3                              ret
00ABF3C6  CC                              int3
00ABF3C7  B8 08 00 00 00                  mov eax, 8
00ABF3CC  EB EE                           jmp 0x140abf3bc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExSizeOfRundownProtectionCacheAware(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5273300)))) <= 1) goto loc_00ABF3C7;
    result = KeGetRecommendedSharedDataAlignment(a1, a2, a3, a4);
    result = (unsigned int)((result) * ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5273300)) + 1)));
loc_00ABF3BC:
    result = (result) + (24);
    v_rsp = (v_rsp) + (32);
    return result;
loc_00ABF3C7:
    goto loc_00ABF3BC;
}
```

## 5. (Beta) C Style

```c
void ExSizeOfRundownProtectionCacheAware(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5076D4)))) <= 1) goto loc_00ABF3C7;
    result = KeGetRecommendedSharedDataAlignment(a1, a2, a3, a4);
    result = (uint32_t)((result) * ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5076D4)) + 1)));
loc_00ABF3BC:
    result = (result) + (24);
    local_rsp = (local_rsp) + (32);
    return result;
loc_00ABF3C7:
    goto loc_00ABF3BC;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ABF3A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00ABF3A0[BB_00ABF3A0]
  bb_00ABF3B1[BB_00ABF3B1]
  bb_00ABF3BC[BB_00ABF3BC]
  bb_00ABF3C6[BB_00ABF3C6]
  bb_00ABF3C7[BB_00ABF3C7]
  bb_00ABF3A0 -->|branch| bb_00ABF3C7
  bb_00ABF3A0 -->|fallthrough| bb_00ABF3B1
  bb_00ABF3B1 -->|flow| bb_00ABF3BC
  bb_00ABF3C6 -->|flow| bb_00ABF3C7
  bb_00ABF3C7 -->|branch| bb_00ABF3BC
```
