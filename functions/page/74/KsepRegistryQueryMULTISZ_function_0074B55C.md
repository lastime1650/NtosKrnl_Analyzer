# KsepRegistryQueryMULTISZ

- RVA: `0x0074B55C`–`0x0074B583` (길이 `39` bytes)
- VA: `0x000000014074B55C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `10`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0074B578` → [KsepRegistryQuerySZ](KsepRegistryQuerySZ_function_0074B58C.md) (function, `0x0074B58C`)

### Direct callers
- [KsepMatchInitBiosInfo](../../init/C3/KsepMatchInitBiosInfo_function_00C3BCB0.md) at `0x00C3BDDC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0074B55C  48 83 EC 38                     sub rsp, 0x38
0074B560  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
0074B565  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0074B56A  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0074B56F  4D 8B C8                        mov r9, r8
0074B572  41 B8 07 00 00 00               mov r8d, 7
0074B578  E8 0F 00 00 00                  call 0x14074b58c
0074B57D  48 83 C4 38                     add rsp, 0x38
0074B581  C3                              ret
0074B582  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepRegistryQueryMULTISZ(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    v_stack_m10 = a5;
    v_stack_m18 = a4;
    result = KsepRegistryQuerySZ(a1, a2, 7, a3);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KsepRegistryQueryMULTISZ(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    v_stack_m10 = Arg5;
    v_stack_m18 = Arg4;
    result = KsepRegistryQuerySZ(Arg1, Arg2, 7, Arg3);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0074B55C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0074B55C[BB_0074B55C]
  bb_0074B582[BB_0074B582]
```
