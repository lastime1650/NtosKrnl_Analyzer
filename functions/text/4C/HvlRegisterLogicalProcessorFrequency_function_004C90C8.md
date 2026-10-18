# HvlRegisterLogicalProcessorFrequency

- RVA: `0x004C90C8`–`0x004C911D` (길이 `85` bytes)
- VA: `0x00000001404C90C8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD438`
- 디코드: `21`개 명령, `85/85` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004C90EC` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004C9106` → [HvlpSetPowerProperty](HvlpSetPowerProperty_function_004C9124.md) (function, `0x004C9124`)

### Direct callers
- [PpmScaleIdleStateValues](../44/PpmScaleIdleStateValues_function_00447674.md) at `0x00447704`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C90C8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004C90CD  57                              push rdi
004C90CE  48 81 EC 40 02 00 00            sub rsp, 0x240
004C90D5  8B FA                           mov edi, edx
004C90D7  8B D9                           mov ebx, ecx
004C90D9  33 C0                           xor eax, eax
004C90DB  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
004C90E0  33 D2                           xor edx, edx
004C90E2  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
004C90E6  41 B8 14 02 00 00               mov r8d, 0x214
004C90EC  E8 4F DB 1F 00                  call 0x1406c6c40
004C90F1  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
004C90F6  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
004C90FE  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
004C9102  89 7C 24 30                     mov dword ptr [rsp + 0x30], edi
004C9106  E8 19 00 00 00                  call 0x1404c9124
004C910B  48 8B 9C 24 50 02 00 00         mov rbx, qword ptr [rsp + 0x250]
004C9113  48 81 C4 40 02 00 00            add rsp, 0x240
004C911A  5F                              pop rdi
004C911B  C3                              ret
004C911C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlRegisterLogicalProcessorFrequency(int a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m218;
    unsigned int v_stack_m220;
    unsigned int v_stack_m224;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (576);
    result = 0;
    a2 = 0;
    v_stack_m224 = 0;
    result = memset(v_stack_m228, a2, 532, a4);
    v_stack_m228 = 2;
    v_stack_m220 = (unsigned int)((unsigned int)(a1));
    v_stack_m218 = (unsigned int)((unsigned int)(a2));
    result = HvlpSetPowerProperty(v_stack_m228, a2, 532, a4);
    v_rsp = (v_rsp) + (576);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlRegisterLogicalProcessorFrequency(int32_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m218;
    uint32_t v_stack_m220;
    uint32_t v_stack_m224;
    uint64_t v_stack_m228;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (576);
    result = 0;
    Arg2 = 0;
    v_stack_m224 = 0;
    result = memset(v_stack_m228, Arg2, 532, a4);
    v_stack_m228 = 2;
    v_stack_m220 = (uint32_t)((uint32_t)(Arg1));
    v_stack_m218 = (uint32_t)((uint32_t)(Arg2));
    result = HvlpSetPowerProperty(v_stack_m228, Arg2, 532, a4);
    local_rsp = (local_rsp) + (576);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C90C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C90C8[BB_004C90C8]
  bb_004C911C[BB_004C911C]
```
