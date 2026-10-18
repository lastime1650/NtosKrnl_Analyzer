# AlpcpReleaseViewAttribute

- RVA: `0x00A63A80`–`0x00A63ACB` (길이 `75` bytes)
- VA: `0x0000000140A63A80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B95C`
- 디코드: `23`개 명령, `75/75` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A63A93` → [AlpcpLockForCachedReferenceBlob](../88/AlpcpLockForCachedReferenceBlob_function_0088A8B0.md) (function, `0x0088A8B0`)
- `0x00A63A9F` → [AlpcpUnlockBlob](../88/AlpcpUnlockBlob_function_0088B990.md) (function, `0x0088B990`)
- `0x00A63AB0` → [AlpcpDereferenceBlobEx](../88/AlpcpDereferenceBlobEx_function_0088AF00.md) (function, `0x0088AF00`)
- `0x00A63AC4` → [AlpcpDeleteView](../88/AlpcpDeleteView_function_0088A26C.md) (function, `0x0088A26C`)

### Direct callers
- [AlpcpReleaseAttributes](../88/AlpcpReleaseAttributes_function_0088D750.md) at `0x0088D79E`
- [AlpcpReleaseMessageAttributesOnCancel](../89/AlpcpReleaseMessageAttributesOnCancel_function_00894030.md) at `0x008940BA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A63A80  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A63A85  57                              push rdi
00A63A86  48 83 EC 20                     sub rsp, 0x20
00A63A8A  48 8B F9                        mov rdi, rcx
00A63A8D  8B DA                           mov ebx, edx
00A63A8F  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00A63A93  E8 18 6E E2 FF                  call 0x14088a8b0
00A63A98  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
00A63A9C  FF 4F 4C                        dec dword ptr [rdi + 0x4c]
00A63A9F  E8 EC 7E E2 FF                  call 0x14088b990
00A63AA4  85 DB                           test ebx, ebx
00A63AA6  75 19                           jne 0x140a63ac1
00A63AA8  BA 01 00 00 00                  mov edx, 1
00A63AAD  48 8B CF                        mov rcx, rdi
00A63AB0  E8 4B 74 E2 FF                  call 0x14088af00
00A63AB5  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A63ABA  48 83 C4 20                     add rsp, 0x20
00A63ABE  5F                              pop rdi
00A63ABF  C3                              ret
00A63AC0  CC                              int3
00A63AC1  48 8B CF                        mov rcx, rdi
00A63AC4  E8 A3 67 E2 FF                  call 0x14088a26c
00A63AC9  EB DD                           jmp 0x140a63aa8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpReleaseViewAttribute(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = AlpcpLockForCachedReferenceBlob(*(unsigned __int64 *)(a1 + 16), a2, a3, a4);
    result = AlpcpUnlockBlob(*(unsigned __int64 *)(a1 + 16), a2, a3, a4);
    if ((unsigned int)((unsigned int)(a2)) != 0) goto loc_00A63AC1;
loc_00A63AA8:
    result = AlpcpDereferenceBlobEx(a1, 1, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_00A63AC1:
    result = AlpcpDeleteView(a1, 1, a3, a4);
    goto loc_00A63AA8;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpReleaseViewAttribute(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = AlpcpLockForCachedReferenceBlob(*(uint64_t *)(arg1 + 0x10), Arg2, a3, a4);
    result = AlpcpUnlockBlob(*(uint64_t *)(arg1 + 0x10), Arg2, a3, a4);
    if ((uint32_t)((uint32_t)(Arg2)) != 0) goto loc_00A63AC1;
loc_00A63AA8:
    result = AlpcpDereferenceBlobEx(Arg1, 1, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_00A63AC1:
    result = AlpcpDeleteView(Arg1, 1, a3, a4);
    goto loc_00A63AA8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x4C` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A63A80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A63A80[BB_00A63A80]
  bb_00A63AA8[BB_00A63AA8]
  bb_00A63AC0[BB_00A63AC0]
  bb_00A63AC1[BB_00A63AC1]
  bb_00A63A80 -->|branch| bb_00A63AC1
  bb_00A63A80 -->|fallthrough| bb_00A63AA8
  bb_00A63AC0 -->|flow| bb_00A63AC1
  bb_00A63AC1 -->|branch| bb_00A63AA8
```
