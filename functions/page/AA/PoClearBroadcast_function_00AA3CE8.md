# PoClearBroadcast

- RVA: `0x00AA3CE8`–`0x00AA3D39` (길이 `81` bytes)
- VA: `0x0000000140AA3CE8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `21`개 명령, `81/81` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00AA3CFA` → [PopResumeDeviceIdle](../../text/4E/PopResumeDeviceIdle_function_004E37D8.md) (function, `0x004E37D8`)
- `0x00AA3D16` → [IoFreePoDeviceNotifyList](../../pagelk/B7/IoFreePoDeviceNotifyList_function_00B7CF84.md) (function, `0x00B7CF84`)
- `0x00AA3D20` → [PpmEndHighPerfRequest](../../text/47/PpmEndHighPerfRequest_function_00477490.md) (function, `0x00477490`)
- `0x00AA3D2D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PopDirectedDripsDestroyBroadcast](PopDirectedDripsDestroyBroadcast_function_00AA3C60.md) at `0x00AA3CD5`
- [PnprWakeDevices](../../pagelk/B6/PnprWakeDevices_function_00B65614.md) at `0x00B65642`
- [PopTransitionSystemPowerStateEx](../../pagelk/B7/PopTransitionSystemPowerStateEx_function_00B7E8C0.md) at `0x00B7EA94`
- [PopTransitionSystemPowerStateEx](../../pagelk/B7/PopTransitionSystemPowerStateEx_function_00B7E8C0.md) at `0x00B7F89E`

### Static image references
- `0x00AA3CEE` → RVA `0x00F0BCD0` (`.data`; read)
- `0x00AA3D08` → RVA `0x00F0BCC0` (`.data`; read)
- `0x00AA3D0F` → RVA `0x00F0BCD0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00AA3CFA` → [PopResumeDeviceIdle](../../text/4E/PopResumeDeviceIdle_function_004E37D8.md) (`PAGE` → `.text`)
  - `0x00AA3D16` → [IoFreePoDeviceNotifyList](../../pagelk/B7/IoFreePoDeviceNotifyList_function_00B7CF84.md) (`PAGE` → `PAGELK`)
  - `0x00AA3D20` → [PpmEndHighPerfRequest](../../text/47/PpmEndHighPerfRequest_function_00477490.md) (`PAGE` → `.text`)
  - `0x00AA3D2D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA3CE8  40 53                           push rbx
00AA3CEA  48 83 EC 20                     sub rsp, 0x20
00AA3CEE  48 8B 1D DB 7F 46 00            mov rbx, qword ptr [rip + 0x467fdb]
00AA3CF5  48 85 DB                        test rbx, rbx
00AA3CF8  74 38                           je 0x140aa3d32
00AA3CFA  E8 D9 FA A3 FF                  call 0x1404e37d8
00AA3CFF  0F 57 C0                        xorps xmm0, xmm0
00AA3D02  48 8D 4B 30                     lea rcx, [rbx + 0x30]
00AA3D06  33 C0                           xor eax, eax
00AA3D08  0F 11 05 B1 7F 46 00            movups xmmword ptr [rip + 0x467fb1], xmm0
00AA3D0F  48 89 05 BA 7F 46 00            mov qword ptr [rip + 0x467fba], rax
00AA3D16  E8 69 92 0D 00                  call 0x140b7cf84
00AA3D1B  B9 02 00 00 00                  mov ecx, 2
00AA3D20  E8 6B 37 9D FF                  call 0x140477490
00AA3D25  BA 50 44 73 73                  mov edx, 0x73734450
00AA3D2A  48 8B CB                        mov rcx, rbx
00AA3D2D  E8 3E EB 0D 00                  call 0x140b82870
00AA3D32  48 83 C4 20                     add rsp, 0x20
00AA3D36  5B                              pop rbx
00AA3D37  C3                              ret
00AA3D38  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PoClearBroadcast(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(v_rip + 4620251) != 0) {
        result = PopResumeDeviceIdle(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(v_rip + 4620251) + 48;
        result = 0;
        *(unsigned __int64 *)(v_rip + 4620209) = v_xmm0;
        *(unsigned __int64 *)(v_rip + 4620218) = 0;
        result = IoFreePoDeviceNotifyList(a1, a2, a3, a4);
        a1 = 2;
        result = PpmEndHighPerfRequest(a1, a2, a3, a4);
        a2 = 0x73734450ULL;
        a1 = *(unsigned __int64 *)(v_rip + 4620251);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
void PoClearBroadcast(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(v_rip + 0x467FDB) != 0) {
        result = PopResumeDeviceIdle(a1, a2, a3, a4);
        a1 = *(uint64_t *)(v_rip + 0x467FDB) + 48;
        result = 0;
        *(uint64_t *)(v_rip + 0x467FB1) = v_xmm0;
        *(uint64_t *)(v_rip + 0x467FBA) = 0;
        result = IoFreePoDeviceNotifyList(a1, a2, a3, a4);
        a1 = 2;
        result = PpmEndHighPerfRequest(a1, a2, a3, a4);
        a2 = 0x73734450ULL;
        a1 = *(uint64_t *)(v_rip + 0x467FDB);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA3CE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AA3CE8[BB_00AA3CE8]
  bb_00AA3CFA[BB_00AA3CFA]
  bb_00AA3D32[BB_00AA3D32]
  bb_00AA3D38[BB_00AA3D38]
  bb_00AA3CE8 -->|branch| bb_00AA3D32
  bb_00AA3CE8 -->|fallthrough| bb_00AA3CFA
  bb_00AA3CFA -->|flow| bb_00AA3D32
```
