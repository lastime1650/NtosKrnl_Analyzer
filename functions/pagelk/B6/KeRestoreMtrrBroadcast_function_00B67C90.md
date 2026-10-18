# KeRestoreMtrrBroadcast

- RVA: `0x00B67C90`–`0x00B67CE3` (길이 `83` bytes)
- VA: `0x0000000140B67C90`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `18`개 명령, `83/83` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00B67CA8` → [KeQueryActiveProcessorCountEx](../../text/24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (function, `0x00249EF0`)
- `0x00B67CD8` → [KeIpiGenericCall](../../text/47/KeIpiGenericCall_function_00471720.md) (function, `0x00471720`)

### Direct callers
- [PnprWakeProcessors](PnprWakeProcessors_function_00B65694.md) at `0x00B656D9`
- [KiInitializeDynamicProcessorDpc](KiInitializeDynamicProcessorDpc_function_00B67A30.md) at `0x00B67B84`
- [KiInitializeMTRR](../../init/C3/KiInitializeMTRR_function_00C39A1C.md) at `0x00C39D41`

### Static image references
- `0x00B67C9A` → RVA `0x00F10EF0` (`.data`; read)
- `0x00B67CB9` → RVA `0x00B67DA0` (`KiLoadMTRRTarget`; read)
- `0x00B67CC4` → RVA `0x00F10F08` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00B67CA8` → [KeQueryActiveProcessorCountEx](../../text/24/KeQueryActiveProcessorCountEx_function_00249EF0.md) (`PAGELK` → `.text`)
  - `0x00B67CD8` → [KeIpiGenericCall](../../text/47/KeIpiGenericCall_function_00471720.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B67C90  48 83 EC 48                     sub rsp, 0x48
00B67C94  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00B67C9A  80 3D 4F 92 3A 00 00            cmp byte ptr [rip + 0x3a924f], 0
00B67CA1  74 3A                           je 0x140b67cdd
00B67CA3  B9 FF FF 00 00                  mov ecx, 0xffff
00B67CA8  E8 43 22 6E FF                  call 0x140249ef0
00B67CAD  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
00B67CB2  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00B67CB7  FF C8                           dec eax
00B67CB9  48 8D 0D E0 00 00 00            lea rcx, [rip + 0xe0]
00B67CC0  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
00B67CC4  48 8D 05 3D 92 3A 00            lea rax, [rip + 0x3a923d]
00B67CCB  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B67CD0  C7 44 24 28 00 00 00 00         mov dword ptr [rsp + 0x28], 0
00B67CD8  E8 43 9A 90 FF                  call 0x140471720
00B67CDD  48 83 C4 48                     add rsp, 0x48
00B67CE1  C3                              ret
00B67CE2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeRestoreMtrrBroadcast(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m24;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    if ((*(unsigned __int8 *)(v_rip + 3838543)) != 0) {
        a1 = 0xFFFFULL;
        result = KeQueryActiveProcessorCountEx(a1, a2, a3, a4);
        a2 = v_stack_m28;
        result = (unsigned int)((result) - 1);
        a1 = v_rip + 224;
        v_stack_m24 = (unsigned int)(result);
        result = v_rip + 3838525;
        v_stack_m18 = result;
        v_stack_m20 = 0;
        result = KeIpiGenericCall(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
void KeRestoreMtrrBroadcast(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m24;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    if ((*(uint8_t *)(v_rip + 0x3A924F)) != 0) {
        a1 = 0xFFFFULL;
        result = KeQueryActiveProcessorCountEx(a1, a2, a3, a4);
        a2 = v_stack_m28;
        result = (uint32_t)((result) - 1);
        a1 = v_rip + 224;
        v_stack_m24 = (uint32_t)(result);
        result = v_rip + 3838525;
        v_stack_m18 = result;
        v_stack_m20 = 0;
        result = KeIpiGenericCall(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B67C90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B67C90[BB_00B67C90]
  bb_00B67CA3[BB_00B67CA3]
  bb_00B67CDD[BB_00B67CDD]
  bb_00B67CE2[BB_00B67CE2]
  bb_00B67C90 -->|branch| bb_00B67CDD
  bb_00B67C90 -->|fallthrough| bb_00B67CA3
  bb_00B67CA3 -->|flow| bb_00B67CDD
```
