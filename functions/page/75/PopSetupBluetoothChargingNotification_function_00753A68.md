# PopSetupBluetoothChargingNotification

- RVA: `0x00753A68`–`0x00753A9C` (길이 `52` bytes)
- VA: `0x0000000140753A68`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `12`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00753A91` → [ExSubscribeWnfStateChange](../9D/ExSubscribeWnfStateChange_function_009D4BC0.md) (function, `0x009D4BC0`)

### Direct callers
- [PoInitSystem](../../init/C7/PoInitSystem_function_00C72358.md) at `0x00C731E1`

### Static image references
- `0x00753A72` → RVA `0x005D1460` (`PopWnfBluetoothChargingCallback`; read)
- `0x00753A81` → RVA `0x00029178` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00753A68  48 83 EC 38                     sub rsp, 0x38
00753A6C  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00753A72  48 8D 05 E7 D9 E7 FF            lea rax, [rip - 0x182619]
00753A79  45 33 C9                        xor r9d, r9d
00753A7C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00753A81  48 8D 15 F0 56 8D FF            lea rdx, [rip - 0x72a910]
00753A88  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00753A8D  45 8D 41 01                     lea r8d, [r9 + 1]
00753A91  E8 2A 11 28 00                  call 0x1409d4bc0
00753A96  48 83 C4 38                     add rsp, 0x38
00753A9A  C3                              ret
00753A9B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopSetupBluetoothChargingNotification(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (56);
    a4 = 0;
    v_stack_m18 = v_rip - 1582617;
    result = ExSubscribeWnfStateChange(v_stack_p8, v_rip - 7514384, a4 + 1, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopSetupBluetoothChargingNotification(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (56);
    Arg4 = 0;
    v_stack_m18 = v_rip - 1582617;
    result = ExSubscribeWnfStateChange(v_stack_p8, v_rip - 7514384, Arg4 + 1, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00753A68&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00753A68[BB_00753A68]
  bb_00753A9B[BB_00753A9B]
```
