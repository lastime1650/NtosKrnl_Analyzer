# SymCryptRsakeyAllocate

- RVA: `0x00522CF4`–`0x00522D3F` (길이 `75` bytes)
- VA: `0x0000000140522CF4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `24`개 명령, `75/75` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00522D08` → [SymCryptSizeofRsakeyFromParams](SymCryptSizeofRsakeyFromParams_function_00523FE4.md) (function, `0x00523FE4`)
- `0x00522D11` → [SymCryptCallbackAlloc](../6A/SymCryptCallbackAlloc_function_006AC530.md) (function, `0x006AC530`)
- `0x00522D23` → [SymCryptRsakeyCreate](SymCryptRsakeyCreate_function_00523594.md) (function, `0x00523594`)

### Direct callers
- [SymCryptRsaSelftest](SymCryptRsaSelftest_function_0052B638.md) at `0x0052B6D6`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00522CF4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00522CF9  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00522CFE  57                              push rdi
00522CFF  48 83 EC 20                     sub rsp, 0x20
00522D03  48 8B F9                        mov rdi, rcx
00522D06  33 DB                           xor ebx, ebx
00522D08  E8 D7 12 00 00                  call 0x140523fe4
00522D0D  8B C8                           mov ecx, eax
00522D0F  8B F0                           mov esi, eax
00522D11  E8 1A 98 18 00                  call 0x1406ac530
00522D16  48 85 C0                        test rax, rax
00522D19  74 10                           je 0x140522d2b
00522D1B  4C 8B C7                        mov r8, rdi
00522D1E  8B D6                           mov edx, esi
00522D20  48 8B C8                        mov rcx, rax
00522D23  E8 6C 08 00 00                  call 0x140523594
00522D28  48 8B D8                        mov rbx, rax
00522D2B  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00522D30  48 8B C3                        mov rax, rbx
00522D33  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00522D38  48 83 C4 20                     add rsp, 0x20
00522D3C  5F                              pop rdi
00522D3D  C3                              ret
00522D3E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptRsakeyAllocate(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    result = SymCryptSizeofRsakeyFromParams(a1, a2, a3, a4);
    result = SymCryptCallbackAlloc((unsigned int)((unsigned int)(result)), a2, a3, a4);
    if (result != 0) {
        a3 = a1;
        a2 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a1 = result;
        result = SymCryptRsakeyCreate(a1, a2, a3, a4);
        v_rbx = result;
    }
    v_rsp = (v_rsp) + (32);
    return v_rbx;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptRsakeyAllocate(int64_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    result = SymCryptSizeofRsakeyFromParams(Arg1, a2, a3, a4);
    result = SymCryptCallbackAlloc((uint32_t)((uint32_t)(result)), a2, a3, a4);
    if (result != 0) {
        a3 = Arg1;
        a2 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg1 = result;
        result = SymCryptRsakeyCreate(Arg1, a2, a3, a4);
        local_rbx = result;
    }
    local_rsp = (local_rsp) + (32);
    return local_rbx;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00522CF4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00522CF4[BB_00522CF4]
  bb_00522D1B[BB_00522D1B]
  bb_00522D2B[BB_00522D2B]
  bb_00522D3E[BB_00522D3E]
  bb_00522CF4 -->|branch| bb_00522D2B
  bb_00522CF4 -->|fallthrough| bb_00522D1B
  bb_00522D1B -->|flow| bb_00522D2B
```
