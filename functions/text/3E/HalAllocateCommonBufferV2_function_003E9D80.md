# HalAllocateCommonBufferV2

- RVA: `0x003E9D80`–`0x003E9DA4` (길이 `36` bytes)
- VA: `0x00000001403E9D80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `10`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003E9D99` → [HalAllocateCommonBufferExV2](HalAllocateCommonBufferExV2_function_003E9DB0.md) (function, `0x003E9DB0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003E9D80  48 83 EC 38                     sub rsp, 0x38
003E9D84  C7 44 24 28 00 00 00 80         mov dword ptr [rsp + 0x28], 0x80000000
003E9D8C  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
003E9D91  4D 8B C8                        mov r9, r8
003E9D94  44 8B C2                        mov r8d, edx
003E9D97  33 D2                           xor edx, edx
003E9D99  E8 12 00 00 00                  call 0x1403e9db0
003E9D9E  48 83 C4 38                     add rsp, 0x38
003E9DA2  C3                              ret
003E9DA3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalAllocateCommonBufferV2(__int64 a1, int a2, __int64 a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned __int8 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    v_stack_m10 = 0x80000000ULL;
    v_stack_m18 = a4;
    a2 = 0;
    result = HalAllocateCommonBufferExV2(a1, a2, (unsigned int)(a2), a3);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalAllocateCommonBufferV2(int64_t Arg1, int32_t Arg2, int64_t Arg3, uint8_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint8_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    v_stack_m10 = 0x80000000ULL;
    v_stack_m18 = Arg4;
    Arg2 = 0;
    result = HalAllocateCommonBufferExV2(Arg1, Arg2, (uint32_t)(Arg2), Arg3);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E9D80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003E9D80[BB_003E9D80]
  bb_003E9DA3[BB_003E9DA3]
```
