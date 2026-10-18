# ExpOsProductContentIdCacheProvider

- RVA: `0x007C8BA0`–`0x007C8BD5` (길이 `53` bytes)
- VA: `0x00000001407C8BA0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `13`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007C8BCA` → [ExpOsProductCacheProviderHelper](ExpOsProductCacheProviderHelper_function_007C8A58.md) (function, `0x007C8A58`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x007C8BC3` → RVA `0x00B4BDF8` (`PAGE`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C8BA0  48 83 EC 48                     sub rsp, 0x48
007C8BA4  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
007C8BA9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007C8BAE  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
007C8BB3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007C8BB8  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
007C8BBD  4D 8B C8                        mov r9, r8
007C8BC0  4C 8B C2                        mov r8, rdx
007C8BC3  48 8D 15 2E 32 38 00            lea rdx, [rip + 0x38322e]
007C8BCA  E8 89 FE FF FF                  call 0x1407c8a58
007C8BCF  48 83 C4 48                     add rsp, 0x48
007C8BD3  C3                              ret
007C8BD4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpOsProductContentIdCacheProvider(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    v_stack_m18 = a6;
    v_stack_m20 = a5;
    v_stack_m28 = a4;
    result = ExpOsProductCacheProviderHelper(a1, v_rip + 3682862, a2, a3);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpOsProductContentIdCacheProvider(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    v_stack_m18 = Arg6;
    v_stack_m20 = Arg5;
    v_stack_m28 = Arg4;
    result = ExpOsProductCacheProviderHelper(Arg1, v_rip + 3682862, Arg2, Arg3);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C8BA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007C8BA0[BB_007C8BA0]
  bb_007C8BD4[BB_007C8BD4]
```
