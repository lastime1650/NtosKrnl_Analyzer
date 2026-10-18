# PiDevCfgCopyDeviceProperties

- RVA: `0x007044F0`–`0x00704517` (길이 `39` bytes)
- VA: `0x00000001407044F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `9`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0070450C` → [PiDevCfgCopyDeviceKey](../99/PiDevCfgCopyDeviceKey_function_00997374.md) (function, `0x00997374`)

### Direct callers
- [PiDevCfgResetDeviceKeyCallback](../73/PiDevCfgResetDeviceKeyCallback_function_007358C0.md) at `0x007358FB`
- [PiDevCfgConfigureDeviceInterface](../96/PiDevCfgConfigureDeviceInterface_function_00963C18.md) at `0x00963E4B`
- [PiDevCfgConfigureDeviceKeyCallback](../A9/PiDevCfgConfigureDeviceKeyCallback_function_00A99890.md) at `0x00A998FC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007044F0  48 83 EC 48                     sub rsp, 0x48
007044F4  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
007044F9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007044FE  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
00704504  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
0070450C  E8 63 2E 29 00                  call 0x140997374
00704511  48 83 C4 48                     add rsp, 0x48
00704515  C3                              ret
00704516  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgCopyDeviceProperties(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    v_stack_m18 = a6;
    v_stack_m28 = 1;
    result = PiDevCfgCopyDeviceKey(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgCopyDeviceProperties(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    v_stack_m18 = Arg6;
    v_stack_m28 = 1;
    result = PiDevCfgCopyDeviceKey(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007044F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007044F0[BB_007044F0]
  bb_00704516[BB_00704516]
```
