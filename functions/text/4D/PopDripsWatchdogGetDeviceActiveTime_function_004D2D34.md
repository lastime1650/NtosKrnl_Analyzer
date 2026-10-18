# PopDripsWatchdogGetDeviceActiveTime

- RVA: `0x004D2D34`–`0x004D2D91` (길이 `93` bytes)
- VA: `0x00000001404D2D34`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `24`개 명령, `93/93` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004D2D50` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x004D2D78` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)

### Direct callers
- [PopDripsWatchdogCallbackHandler](../../page/76/PopDripsWatchdogCallbackHandler_function_0076C1C0.md) at `0x0076C2B9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004D2D34  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004D2D39  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
004D2D3E  57                              push rdi
004D2D3F  48 83 EC 20                     sub rsp, 0x20
004D2D43  48 8D B1 80 02 00 00            lea rsi, [rcx + 0x280]
004D2D4A  48 8B F9                        mov rdi, rcx
004D2D4D  48 8B CE                        mov rcx, rsi
004D2D50  E8 1B 57 D3 FF                  call 0x140208470
004D2D55  33 DB                           xor ebx, ebx
004D2D57  8A D0                           mov dl, al
004D2D59  38 9F 88 02 00 00               cmp byte ptr [rdi + 0x288], bl
004D2D5F  74 14                           je 0x1404d2d75
004D2D61  48 A1 08 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000008]
004D2D6B  48 8B D8                        mov rbx, rax
004D2D6E  48 2B 9F 98 02 00 00            sub rbx, qword ptr [rdi + 0x298]
004D2D75  48 8B CE                        mov rcx, rsi
004D2D78  E8 23 FE EB FF                  call 0x140392ba0
004D2D7D  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
004D2D82  48 8B C3                        mov rax, rbx
004D2D85  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004D2D8A  48 83 C4 20                     add rsp, 0x20
004D2D8E  5F                              pop rdi
004D2D8F  C3                              ret
004D2D90  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDripsWatchdogGetDeviceActiveTime(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(a1 + 640, a2, a3, a4);
    v_rbx = 0;
    if ((*(unsigned __int8 *)(a1 + 648)) != 0) {
        v_rbx = result;
        v_rbx = (v_rbx) - (*(unsigned __int64 *)(a1 + 664));
    }
    result = KeReleaseSpinLock(a1 + 640, (unsigned __int8)(result), a3, a4);
    v_rsp = (v_rsp) + (32);
    return v_rbx;
}
```

## 5. (Beta) C Style

```c
int64_t PopDripsWatchdogGetDeviceActiveTime(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(Arg1 + 640, a2, a3, a4);
    local_rbx = 0;
    if ((*(uint8_t *)(arg1 + 0x288)) != 0) {
        local_rbx = result;
        local_rbx = (local_rbx) - (*(uint64_t *)(arg1 + 0x298));
    }
    result = KeReleaseSpinLock(Arg1 + 640, (uint8_t)(result), a3, a4);
    local_rsp = (local_rsp) + (32);
    return local_rbx;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x280` | `64` | `R` |
| `Arg1` | `+ 0x288` | `8` | `R` |
| `Arg1` | `+ 0x298` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004D2D34&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004D2D34[BB_004D2D34]
  bb_004D2D61[BB_004D2D61]
  bb_004D2D75[BB_004D2D75]
  bb_004D2D90[BB_004D2D90]
  bb_004D2D34 -->|branch| bb_004D2D75
  bb_004D2D34 -->|fallthrough| bb_004D2D61
  bb_004D2D61 -->|flow| bb_004D2D75
```
