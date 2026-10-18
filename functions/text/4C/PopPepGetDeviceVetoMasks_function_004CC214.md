# PopPepGetDeviceVetoMasks

- RVA: `0x004CC214`–`0x004CC280` (길이 `108` bytes)
- VA: `0x00000001404CC214`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C954`
- 디코드: `28`개 명령, `108/108` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004CC235` → [ExAcquireSpinLockShared](../24/ExAcquireSpinLockShared_function_0024DCE0.md) (function, `0x0024DCE0`)
- `0x004CC262` → [ExReleaseSpinLockShared](../2F/ExReleaseSpinLockShared_function_002F0EF0.md) (function, `0x002F0EF0`)

### Direct callers
- [PopFxTraceDeviceRegistration](../../page/A6/PopFxTraceDeviceRegistration_function_00A6F888.md) at `0x00A6F907`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004CC214  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004CC219  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
004CC21E  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
004CC223  57                              push rdi
004CC224  48 83 EC 20                     sub rsp, 0x20
004CC228  48 8B D9                        mov rbx, rcx
004CC22B  48 8B EA                        mov rbp, rdx
004CC22E  48 83 C1 40                     add rcx, 0x40
004CC232  40 32 FF                        xor dil, dil
004CC235  E8 A6 1A D8 FF                  call 0x14024dce0
004CC23A  83 BB AC 00 00 00 02            cmp dword ptr [rbx + 0xac], 2
004CC241  8A D0                           mov dl, al
004CC243  75 19                           jne 0x1404cc25e
004CC245  F2 0F 10 83 90 00 00 00         movsd xmm0, qword ptr [rbx + 0x90]
004CC24D  40 B7 01                        mov dil, 1
004CC250  F2 0F 11 45 00                  movsd qword ptr [rbp], xmm0
004CC255  8B 83 98 00 00 00               mov eax, dword ptr [rbx + 0x98]
004CC25B  89 45 08                        mov dword ptr [rbp + 8], eax
004CC25E  48 8D 4B 40                     lea rcx, [rbx + 0x40]
004CC262  E8 89 4C E2 FF                  call 0x1402f0ef0
004CC267  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004CC26C  40 8A C7                        mov al, dil
004CC26F  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
004CC274  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
004CC279  48 83 C4 20                     add rsp, 0x20
004CC27D  5F                              pop rdi
004CC27E  C3                              ret
004CC27F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPepGetDeviceVetoMasks(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (64);
    v_rdi = 0;
    result = ExAcquireSpinLockShared(a1, a2, a3, a4);
    if ((*(unsigned int *)(a1 + 172)) == 2) {
        v_rdi = 1;
        *(unsigned __int64 *)(a2) = v_xmm0;
        result = *(unsigned int *)(a1 + 152);
        *(unsigned int *)(a2 + 8) = (unsigned int)(result);
    }
    result = ExReleaseSpinLockShared(a1 + 64, (unsigned __int8)(result), a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_rdi);
}
```

## 5. (Beta) C Style

```c
int64_t PopPepGetDeviceVetoMasks(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (64);
    local_rdi = 0;
    result = ExAcquireSpinLockShared(Arg1, Arg2, a3, a4);
    if ((*(uint32_t *)(arg1 + 0xAC)) == 2) {
        local_rdi = 1;
        *(uint64_t *)(arg2) = v_xmm0;
        result = *(uint32_t *)(arg1 + 0x98);
        *(uint32_t *)(arg2 + 0x8) = (uint32_t)(result);
    }
    result = ExReleaseSpinLockShared(Arg1 + 64, (uint8_t)(result), a3, a4);
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(local_rdi);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x90` | `64` | `R` |
| `Arg1` | `+ 0x98` | `32` | `R` |
| `Arg1` | `+ 0xAC` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x8` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004CC214&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004CC214[BB_004CC214]
  bb_004CC245[BB_004CC245]
  bb_004CC25E[BB_004CC25E]
  bb_004CC27F[BB_004CC27F]
  bb_004CC214 -->|branch| bb_004CC25E
  bb_004CC214 -->|fallthrough| bb_004CC245
  bb_004CC245 -->|flow| bb_004CC25E
```
