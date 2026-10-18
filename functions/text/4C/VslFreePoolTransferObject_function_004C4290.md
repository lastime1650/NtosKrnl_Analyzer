# VslFreePoolTransferObject

- RVA: `0x004C4290`–`0x004C42D6` (길이 `70` bytes)
- VA: `0x00000001404C4290`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BE4`
- 디코드: `23`개 명령, `70/70` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004C42AF` → [VslpUnlockPagesForTransfer](../29/VslpUnlockPagesForTransfer_function_0029EE4C.md) (function, `0x0029EE4C`)
- `0x004C42B9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [VslFinishSecureImageValidation](../58/VslFinishSecureImageValidation_function_0058FEB0.md) at `0x0058FF6C`
- [sub_006F88AE](../6F/Unknown_function_006F88AE.md) at `0x006F8B58`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004C42B9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C4290  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004C4295  57                              push rdi
004C4296  48 83 EC 20                     sub rsp, 0x20
004C429A  48 8B D9                        mov rbx, rcx
004C429D  48 8B 09                        mov rcx, qword ptr [rcx]
004C42A0  8B 79 2C                        mov edi, dword ptr [rcx + 0x2c]
004C42A3  48 03 79 20                     add rdi, qword ptr [rcx + 0x20]
004C42A7  48 85 D2                        test rdx, rdx
004C42AA  75 21                           jne 0x1404c42cd
004C42AC  48 8B CB                        mov rcx, rbx
004C42AF  E8 98 AB DD FF                  call 0x14029ee4c
004C42B4  33 D2                           xor edx, edx
004C42B6  48 8B CB                        mov rcx, rbx
004C42B9  E8 B2 E5 6B 00                  call 0x140b82870
004C42BE  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004C42C3  48 8B C7                        mov rax, rdi
004C42C6  48 83 C4 20                     add rsp, 0x20
004C42CA  5F                              pop rdi
004C42CB  C3                              ret
004C42CC  CC                              int3
004C42CD  44 8B 41 28                     mov r8d, dword ptr [rcx + 0x28]
004C42D1  4C 89 02                        mov qword ptr [rdx], r8
004C42D4  EB D6                           jmp 0x1404c42ac
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VslFreePoolTransferObject(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_rdi = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1) + 44))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 32));
    if (a2 != 0) goto loc_004C42CD;
loc_004C42AC:
    result = VslpUnlockPagesForTransfer(a1, a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return v_rdi;
loc_004C42CD:
    *(unsigned __int64 *)(a2) = (unsigned int)(*(unsigned int *)(a1 + 40));
    goto loc_004C42AC;
}
```

## 5. (Beta) C Style

```c
int64_t VslFreePoolTransferObject(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    local_rdi = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1) + 0x2C))) + (*(uint64_t *)(*(uint64_t *)(arg1) + 0x20));
    if (Arg2 != 0) goto loc_004C42CD;
loc_004C42AC:
    result = VslpUnlockPagesForTransfer(Arg1, Arg2, a3, a4);
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return local_rdi;
loc_004C42CD:
    *(uint64_t *)(Arg2) = (uint32_t)(*(uint32_t *)(arg1 + 0x28));
    goto loc_004C42AC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C4290&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C4290[BB_004C4290]
  bb_004C42AC[BB_004C42AC]
  bb_004C42CC[BB_004C42CC]
  bb_004C42CD[BB_004C42CD]
  bb_004C4290 -->|branch| bb_004C42CD
  bb_004C4290 -->|fallthrough| bb_004C42AC
  bb_004C42CC -->|flow| bb_004C42CD
  bb_004C42CD -->|branch| bb_004C42AC
```
