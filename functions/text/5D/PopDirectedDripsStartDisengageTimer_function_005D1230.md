# PopDirectedDripsStartDisengageTimer

- RVA: `0x005D1230`–`0x005D12D0` (길이 `160` bytes)
- VA: `0x00000001405D1230`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00066400`
- 디코드: `42`개 명령, `160/160` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005D125D` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x005D1277` → [KeCancelTimer2](../3A/KeCancelTimer2_function_003A01E0.md) (function, `0x003A01E0`)
- `0x005D128B` → [PopDirectedDripsSetDisengageReason](../47/PopDirectedDripsSetDisengageReason_function_00478D60.md) (function, `0x00478D60`)
- `0x005D12A6` → [KeSetTimer2](../3A/KeSetTimer2_function_003A08E0.md) (function, `0x003A08E0`)
- `0x005D12B5` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)

### Direct callers
- [PoFxNotifySurprisePowerOn](../26/PoFxNotifySurprisePowerOn_function_0026E620.md) at `0x0026E6A4`
- [PopRequestCompletion](../26/PopRequestCompletion_function_0026EEF0.md) at `0x0026EFDB`

### Static image references
- `0x005D124B` → RVA `0x00F0EBA8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D1230  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005D1235  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
005D123A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
005D123F  57                              push rdi
005D1240  48 83 EC 30                     sub rsp, 0x30
005D1244  48 63 C1                        movsxd rax, ecx
005D1247  48 8D 1C 80                     lea rbx, [rax + rax*4]
005D124B  48 8D 05 56 D9 93 00            lea rax, [rip + 0x93d956]
005D1252  48 C1 E3 05                     shl rbx, 5
005D1256  48 03 D8                        add rbx, rax
005D1259  48 8D 4B 08                     lea rcx, [rbx + 8]
005D125D  E8 0E 72 C3 FF                  call 0x140208470
005D1262  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005D1268  48 8D 4B 18                     lea rcx, [rbx + 0x18]
005D126C  48 83 4C 24 28 FF               or qword ptr [rsp + 0x28], 0xffffffffffffffff
005D1272  33 D2                           xor edx, edx
005D1274  40 8A E8                        mov bpl, al
005D1277  E8 64 EF DC FF                  call 0x1403a01e0
005D127C  84 C0                           test al, al
005D127E  75 10                           jne 0x1405d1290
005D1280  FF 43 14                        inc dword ptr [rbx + 0x14]
005D1283  83 7B 14 01                     cmp dword ptr [rbx + 0x14], 1
005D1287  75 07                           jne 0x1405d1290
005D1289  8B 0B                           mov ecx, dword ptr [rbx]
005D128B  E8 D0 7A EA FF                  call 0x140478d60
005D1290  8B 43 04                        mov eax, dword ptr [rbx + 4]
005D1293  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
005D1298  48 69 D0 80 69 67 FF            imul rdx, rax, -0x989680
005D129F  45 33 C0                        xor r8d, r8d
005D12A2  48 8D 4B 18                     lea rcx, [rbx + 0x18]
005D12A6  E8 35 F6 DC FF                  call 0x1403a08e0
005D12AB  FF 43 10                        inc dword ptr [rbx + 0x10]
005D12AE  48 8D 4B 08                     lea rcx, [rbx + 8]
005D12B2  40 8A D5                        mov dl, bpl
005D12B5  E8 E6 18 DC FF                  call 0x140392ba0
005D12BA  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
005D12BF  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
005D12C4  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
005D12C9  48 83 C4 30                     add rsp, 0x30
005D12CD  5F                              pop rdi
005D12CE  C3                              ret
005D12CF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDirectedDripsStartDisengageTimer(int a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    v_rbx = ((int)(a1) + (int)(a1) * 4) << (5);
    v_rbx = (v_rbx) + (v_rip + 9689430);
    result = KeAcquireSpinLockRaiseToDpc(v_rbx + 8, a2, a3, a4);
    a2 = 0;
    result = KeCancelTimer2(v_rbx + 24, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_005D1290;
    if ((*(unsigned int *)(v_rbx + 20)) == 1) {
        a1 = *(unsigned int *)(v_rbx);
        result = PopDirectedDripsSetDisengageReason(a1, a2, a3, a4);
    }
    a2 = (a2) * ((unsigned int)(*(unsigned int *)(v_rbx + 4)));
    a3 = 0;
    result = KeSetTimer2(v_rbx + 24, a2, a3, v_stack_m18);
    result = KeReleaseSpinLock(v_rbx + 8, (unsigned __int8)((unsigned __int8)(result)), a3, v_stack_m18);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDirectedDripsStartDisengageTimer(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    local_rbx = ((int32_t)(Arg1) + (int32_t)(Arg1) * 4) << (5);
    local_rbx = (local_rbx) + (v_rip + 9689430);
    result = KeAcquireSpinLockRaiseToDpc(local_rbx + 8, Arg2, Arg3, a4);
    Arg2 = 0;
    result = KeCancelTimer2(local_rbx + 24, Arg2, Arg3, a4);
    if ((uint8_t)(result) != 0) goto loc_005D1290;
    if ((*(uint32_t *)(local_rbx + 0x14)) == 1) {
        Arg1 = *(uint32_t *)(local_rbx);
        result = PopDirectedDripsSetDisengageReason(Arg1, Arg2, Arg3, a4);
    }
    Arg2 = (Arg2) * ((uint32_t)(*(uint32_t *)(local_rbx + 0x4)));
    Arg3 = 0;
    result = KeSetTimer2(local_rbx + 24, Arg2, Arg3, v_stack_m18);
    result = KeReleaseSpinLock(local_rbx + 8, (uint8_t)((uint8_t)(result)), Arg3, v_stack_m18);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rax*4` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D1230&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D1230[BB_005D1230]
  bb_005D1280[BB_005D1280]
  bb_005D1289[BB_005D1289]
  bb_005D1290[BB_005D1290]
  bb_005D12CF[BB_005D12CF]
  bb_005D1230 -->|branch| bb_005D1290
  bb_005D1230 -->|fallthrough| bb_005D1280
  bb_005D1280 -->|branch| bb_005D1290
  bb_005D1280 -->|fallthrough| bb_005D1289
  bb_005D1289 -->|flow| bb_005D1290
```
