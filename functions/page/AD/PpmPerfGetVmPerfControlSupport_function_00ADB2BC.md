# PpmPerfGetVmPerfControlSupport

- RVA: `0x00ADB2BC`–`0x00ADB32E` (길이 `114` bytes)
- VA: `0x0000000140ADB2BC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `28`개 명령, `114/114` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00ADB2CC` → [PpmAcquireLock](../../text/2D/PpmAcquireLock_function_002D9AA4.md) (function, `0x002D9AA4`)
- `0x00ADB322` → [PpmReleaseLock](../../text/2D/PpmReleaseLock_function_002DA428.md) (function, `0x002DA428`)

### Direct callers
- [PopPowerInformationInternal](../A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8CBD2`

### Static image references
- `0x00ADB2C5` → RVA `0x00F0CC00` (`.data`; read)
- `0x00ADB2D6` → RVA `0x00FC6AEC` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00ADB2CC` → [PpmAcquireLock](../../text/2D/PpmAcquireLock_function_002D9AA4.md) (`PAGE` → `.text`)
  - `0x00ADB322` → [PpmReleaseLock](../../text/2D/PpmReleaseLock_function_002DA428.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ADB2BC  40 53                           push rbx
00ADB2BE  48 83 EC 20                     sub rsp, 0x20
00ADB2C2  48 8B D9                        mov rbx, rcx
00ADB2C5  48 8D 0D 34 19 43 00            lea rcx, [rip + 0x431934]
00ADB2CC  E8 D3 E7 7F FF                  call 0x1402d9aa4
00ADB2D1  33 C0                           xor eax, eax
00ADB2D3  0F 57 C0                        xorps xmm0, xmm0
00ADB2D6  38 05 10 B8 4E 00               cmp byte ptr [rip + 0x4eb810], al
00ADB2DC  0F 11 03                        movups xmmword ptr [rbx], xmm0
00ADB2DF  89 43 10                        mov dword ptr [rbx + 0x10], eax
00ADB2E2  74 37                           je 0x140adb31b
00ADB2E4  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
00ADB2ED  48 8B 90 B0 89 00 00            mov rdx, qword ptr [rax + 0x89b0]
00ADB2F4  C6 03 01                        mov byte ptr [rbx], 1
00ADB2F7  8B 82 F4 01 00 00               mov eax, dword ptr [rdx + 0x1f4]
00ADB2FD  89 43 10                        mov dword ptr [rbx + 0x10], eax
00ADB300  8B 82 F8 01 00 00               mov eax, dword ptr [rdx + 0x1f8]
00ADB306  89 43 04                        mov dword ptr [rbx + 4], eax
00ADB309  8B 82 FC 01 00 00               mov eax, dword ptr [rdx + 0x1fc]
00ADB30F  89 43 08                        mov dword ptr [rbx + 8], eax
00ADB312  8B 82 00 02 00 00               mov eax, dword ptr [rdx + 0x200]
00ADB318  89 43 0C                        mov dword ptr [rbx + 0xc], eax
00ADB31B  48 8D 0D DE 18 43 00            lea rcx, [rip + 0x4318de]
00ADB322  E8 01 F1 7F FF                  call 0x1402da428
00ADB327  48 83 C4 20                     add rsp, 0x20
00ADB32B  5B                              pop rbx
00ADB32C  C3                              ret
00ADB32D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmPerfGetVmPerfControlSupport(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = PpmAcquireLock(v_rip + 4397364, a2, a3, a4);
    result = 0;
    *(unsigned __int64 *)(a1) = v_xmm0;
    *(unsigned int *)(a1 + 16) = 0;
    if ((*(unsigned __int8 *)(v_rip + 5158928)) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 32));
        a2 = *(unsigned __int64 *)(result + 35248);
        *(unsigned __int8 *)(a1) = 1;
        result = *(unsigned int *)(a2 + 500);
        *(unsigned int *)(a1 + 16) = (unsigned int)(result);
        result = *(unsigned int *)(a2 + 504);
        *(unsigned int *)(a1 + 4) = (unsigned int)(result);
        result = *(unsigned int *)(a2 + 508);
        *(unsigned int *)(a1 + 8) = (unsigned int)(result);
        result = *(unsigned int *)(a2 + 512);
        *(unsigned int *)(a1 + 12) = (unsigned int)(result);
    }
    result = PpmReleaseLock(v_rip + 4397278, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmPerfGetVmPerfControlSupport(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = PpmAcquireLock(v_rip + 4397364, a2, a3, a4);
    result = 0;
    *(uint64_t *)(arg1) = v_xmm0;
    *(uint32_t *)(arg1 + 0x10) = 0;
    if ((*(uint8_t *)(v_rip + 0x4EB810)) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x20));
        a2 = *(uint64_t *)(result + 0x89B0);
        *(uint8_t *)(arg1) = 1;
        result = *(uint32_t *)(a2 + 0x1F4);
        *(uint32_t *)(arg1 + 0x10) = (uint32_t)(result);
        result = *(uint32_t *)(a2 + 0x1F8);
        *(uint32_t *)(arg1 + 0x4) = (uint32_t)(result);
        result = *(uint32_t *)(a2 + 0x1FC);
        *(uint32_t *)(arg1 + 0x8) = (uint32_t)(result);
        result = *(uint32_t *)(a2 + 0x200);
        *(uint32_t *)(arg1 + 0xC) = (uint32_t)(result);
    }
    result = PpmReleaseLock(v_rip + 4397278, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `W` |
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0xC` | `32` | `W` |
| `Arg1` | `+ 0x10` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ADB2BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00ADB2BC[BB_00ADB2BC]
  bb_00ADB2E4[BB_00ADB2E4]
  bb_00ADB31B[BB_00ADB31B]
  bb_00ADB32D[BB_00ADB32D]
  bb_00ADB2BC -->|branch| bb_00ADB31B
  bb_00ADB2BC -->|fallthrough| bb_00ADB2E4
  bb_00ADB2E4 -->|flow| bb_00ADB31B
```
