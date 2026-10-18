# CmpCallCallBacks

- RVA: `0x00865E10`–`0x00865E3E` (길이 `46` bytes)
- VA: `0x0000000140865E10`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `12`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00865E33` → [CmpCallCallBacksEx](CmpCallCallBacksEx_function_00865F40.md) (function, `0x00865F40`)

### Direct callers
- [CmpDoQueryKeyName](../../text/45/CmpDoQueryKeyName_function_00456664.md) at `0x004567CE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00865E10  48 83 EC 48                     sub rsp, 0x48
00865E14  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00865E19  45 33 C0                        xor r8d, r8d
00865E1C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00865E21  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00865E26  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00865E2B  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00865E30  41 B1 01                        mov r9b, 1
00865E33  E8 08 01 00 00                  call 0x140865f40
00865E38  48 83 C4 48                     add rsp, 0x48
00865E3C  C3                              ret
00865E3D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpCallCallBacks(__int64 a1, __int64 a2, int a3, int a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    a3 = 0;
    v_stack_m18 = a6;
    v_stack_m20 = a5;
    v_stack_m28 = a4;
    result = CmpCallCallBacksEx(a1, a2, a3, 1);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpCallCallBacks(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    Arg3 = 0;
    v_stack_m18 = Arg6;
    v_stack_m20 = Arg5;
    v_stack_m28 = Arg4;
    result = CmpCallCallBacksEx(Arg1, Arg2, Arg3, 1);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00865E10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00865E10[BB_00865E10]
  bb_00865E3D[BB_00865E3D]
```
