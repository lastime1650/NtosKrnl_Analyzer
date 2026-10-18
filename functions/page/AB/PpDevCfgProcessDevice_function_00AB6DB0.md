# PpDevCfgProcessDevice

- RVA: `0x00AB6DB0`–`0x00AB6DCF` (길이 `31` bytes)
- VA: `0x0000000140AB6DB0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `9`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AB6DC8` → [PiDevCfgProcessDevice](../97/PiDevCfgProcessDevice_function_00976D34.md) (function, `0x00976D34`)

### Direct callers
- [PiConfigureDevice](../72/PiConfigureDevice_function_0072D38C.md) at `0x0072D414`
- [PiProcessNewDeviceNode](../A2/PiProcessNewDeviceNode_function_00A28F20.md) at `0x00A2A1C2`
- [sub_00B1F622](../B1/Unknown_function_00B1F622.md) at `0x00B1F89A`
- [sub_00B420B0](../B4/Unknown_function_00B420B0.md) at `0x00B42344`

### Static image references
- `0x00AB6DB4` → RVA `0x00FD8054` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB6DB0  48 83 EC 28                     sub rsp, 0x28
00AB6DB4  83 3D 99 12 52 00 00            cmp dword ptr [rip + 0x521299], 0
00AB6DBB  75 0B                           jne 0x140ab6dc8
00AB6DBD  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00AB6DC2  48 83 C4 28                     add rsp, 0x28
00AB6DC6  C3                              ret
00AB6DC7  CC                              int3
00AB6DC8  E8 67 FF EB FF                  call 0x140976d34
00AB6DCD  EB F3                           jmp 0x140ab6dc2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpDevCfgProcessDevice(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(v_rip + 5378713)) != 0) goto loc_00AB6DC8;
loc_00AB6DC2:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(0xC00000BBULL);
loc_00AB6DC8:
    result = PiDevCfgProcessDevice(a1, a2, a3, a4);
    goto loc_00AB6DC2;
}
```

## 5. (Beta) C Style

```c
void PpDevCfgProcessDevice(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(v_rip + 0x521299)) != 0) goto loc_00AB6DC8;
loc_00AB6DC2:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(0xC00000BBULL);
loc_00AB6DC8:
    result = PiDevCfgProcessDevice(a1, a2, a3, a4);
    goto loc_00AB6DC2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB6DB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB6DB0[BB_00AB6DB0]
  bb_00AB6DBD[BB_00AB6DBD]
  bb_00AB6DC2[BB_00AB6DC2]
  bb_00AB6DC7[BB_00AB6DC7]
  bb_00AB6DC8[BB_00AB6DC8]
  bb_00AB6DB0 -->|branch| bb_00AB6DC8
  bb_00AB6DB0 -->|fallthrough| bb_00AB6DBD
  bb_00AB6DBD -->|flow| bb_00AB6DC2
  bb_00AB6DC7 -->|flow| bb_00AB6DC8
  bb_00AB6DC8 -->|branch| bb_00AB6DC2
```
