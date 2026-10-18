# CcInitializeCacheMapEx

- RVA: `0x0057B1F0`–`0x0057B217` (길이 `39` bytes)
- VA: `0x000000014057B1F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `10`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0057B20C` → [CcInitializeCacheMapInternal](../3C/CcInitializeCacheMapInternal_function_003CC720.md) (function, `0x003CC720`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0057B1F0  48 83 EC 48                     sub rsp, 0x48
0057B1F4  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
0057B1F8  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0057B1FC  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0057B201  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0057B206  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0057B20C  E8 0F 15 E5 FF                  call 0x1403cc720
0057B211  48 83 C4 48                     add rsp, 0x48
0057B215  C3                              ret
0057B216  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcInitializeCacheMapEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    v_stack_m18 = (unsigned int)((unsigned int)(a6));
    v_stack_m20 = a5;
    result = CcInitializeCacheMapInternal(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcInitializeCacheMapEx(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    v_stack_m18 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m20 = Arg5;
    result = CcInitializeCacheMapInternal(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0057B1F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0057B1F0[BB_0057B1F0]
  bb_0057B216[BB_0057B216]
```
