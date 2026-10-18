# PiPnpRtlGetDeviceNtPropertyRoutine

- RVA: `0x00A2CB90`–`0x00A2CBC8` (길이 `56` bytes)
- VA: `0x0000000140A2CB90`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C80`
- 디코드: `17`개 명령, `56/56` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A2CBBC` → [PlugPlayGetDeviceProperty](PlugPlayGetDeviceProperty_function_00A2CBD0.md) (function, `0x00A2CBD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A2CB90  40 53                           push rbx
00A2CB92  48 83 EC 30                     sub rsp, 0x30
00A2CB96  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00A2CB9A  4D 8B D1                        mov r10, r9
00A2CB9D  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
00A2CBA2  45 8B D8                        mov r11d, r8d
00A2CBA5  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00A2CBA9  48 8B CA                        mov rcx, rdx
00A2CBAC  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00A2CBB1  4D 8B C2                        mov r8, r10
00A2CBB4  41 8B D3                        mov edx, r11d
00A2CBB7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A2CBBC  E8 0F 00 00 00                  call 0x140a2cbd0
00A2CBC1  48 83 C4 30                     add rsp, 0x30
00A2CBC5  5B                              pop rbx
00A2CBC6  C3                              ret
00A2CBC7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiPnpRtlGetDeviceNtPropertyRoutine(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5, __int64 a6, unsigned int a7)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (48);
    v_stack_m10 = (unsigned int)((unsigned int)(a7));
    v_stack_m18 = a6;
    result = PlugPlayGetDeviceProperty(a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4, (unsigned int)(a5));
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiPnpRtlGetDeviceNtPropertyRoutine(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6, uint32_t Arg7)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (48);
    v_stack_m10 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m18 = Arg6;
    result = PlugPlayGetDeviceProperty(Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4, (uint32_t)(Arg5));
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A2CB90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A2CB90[BB_00A2CB90]
  bb_00A2CBC7[BB_00A2CBC7]
```
