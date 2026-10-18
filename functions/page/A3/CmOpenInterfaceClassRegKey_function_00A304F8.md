# CmOpenInterfaceClassRegKey

- RVA: `0x00A304F8`–`0x00A30538` (길이 `64` bytes)
- VA: `0x0000000140A304F8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `15`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A3052D` → [CmOpenCommonClassRegKey](../8E/CmOpenCommonClassRegKey_function_008EFF5C.md) (function, `0x008EFF5C`)

### Direct callers
- [CmDeleteInterfaceClassMappedPropertyFromRegValue](../82/CmDeleteInterfaceClassMappedPropertyFromRegValue_function_0082FD08.md) at `0x0082FDD1`
- [CmSetInterfaceClassMappedPropertyFromRegValue](../83/CmSetInterfaceClassMappedPropertyFromRegValue_function_0083164C.md) at `0x0083172A`
- [_PnpDispatchInterfaceClass](../99/_PnpDispatchInterfaceClass_function_00993BD0.md) at `0x00993EA6`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A304F8  48 83 EC 48                     sub rsp, 0x48
00A304FC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00A30504  45 33 C9                        xor r9d, r9d
00A30507  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A3050C  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00A30514  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A30519  8A 44 24 78                     mov al, byte ptr [rsp + 0x78]
00A3051D  45 8D 41 40                     lea r8d, [r9 + 0x40]
00A30521  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00A30525  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00A30529  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00A3052D  E8 2A FA EB FF                  call 0x1408eff5c
00A30532  48 83 C4 48                     add rsp, 0x48
00A30536  C3                              ret
00A30537  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmOpenInterfaceClassRegKey(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5, unsigned __int8 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int8 v_stack_m20;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    a4 = 0;
    v_stack_m10 = a8;
    v_stack_m18 = a7;
    v_stack_m20 = a6;
    v_stack_m28 = (unsigned int)((unsigned int)(a5));
    result = CmOpenCommonClassRegKey(a1, a2, a4 + 64, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmOpenInterfaceClassRegKey(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5, uint8_t Arg6, int64_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint8_t v_stack_m20;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    Arg4 = 0;
    v_stack_m10 = Arg8;
    v_stack_m18 = Arg7;
    v_stack_m20 = Arg6;
    v_stack_m28 = (uint32_t)((uint32_t)(Arg5));
    result = CmOpenCommonClassRegKey(Arg1, Arg2, Arg4 + 64, Arg4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A304F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A304F8[BB_00A304F8]
  bb_00A30537[BB_00A30537]
```
