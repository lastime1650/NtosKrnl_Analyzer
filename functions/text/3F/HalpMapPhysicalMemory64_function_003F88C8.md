# HalpMapPhysicalMemory64

- RVA: `0x003F88C8`–`0x003F88EB` (길이 `35` bytes)
- VA: `0x00000001403F88C8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `9`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003F88E0` → [HalpMap](HalpMap_function_003F88F4.md) (function, `0x003F88F4`)

### Direct callers
- [HalpCheckLowMemoryPreSleep](../../pagelk/B5/HalpCheckLowMemoryPreSleep_function_00B5EB88.md) at `0x00B5EC7D`
- [HalpCheckLowMemoryPostSleep](../../pagelk/B7/HalpCheckLowMemoryPostSleep_function_00B7A458.md) at `0x00B7A515`
- [HalpAllocateScratchMemory](../../pagekd/B8/HalpAllocateScratchMemory_function_00B854B0.md) at `0x00B85550`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003F88C8  48 83 EC 38                     sub rsp, 0x38
003F88CC  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
003F88D2  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
003F88D7  45 8A C8                        mov r9b, r8b
003F88DA  41 B8 01 00 00 00               mov r8d, 1
003F88E0  E8 0F 00 00 00                  call 0x1403f88f4
003F88E5  48 83 C4 38                     add rsp, 0x38
003F88E9  C3                              ret
003F88EA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpMapPhysicalMemory64(__int64 a1, __int64 a2, unsigned __int8 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m18;

    v_rsp = (v_rsp) - (56);
    v_stack_m18 = a4;
    result = HalpMap(a1, a2, 1, a3);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpMapPhysicalMemory64(int64_t Arg1, int64_t Arg2, uint8_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    v_stack_m18 = Arg4;
    result = HalpMap(Arg1, Arg2, 1, Arg3);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003F88C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003F88C8[BB_003F88C8]
  bb_003F88EA[BB_003F88EA]
```
