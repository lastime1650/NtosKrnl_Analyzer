# MiSetInPagePrefetchPriority

- RVA: `0x0036A974`–`0x0036A99C` (길이 `40` bytes)
- VA: `0x000000014036A974`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0036A991` → [MiSetInPagePriority](MiSetInPagePriority_function_0036A9A4.md) (function, `0x0036A9A4`)

### Direct callers
- [MiResolveMappedFileFault](MiResolveMappedFileFault_function_0036B640.md) at `0x0036BCE5`
- [MiResolvePageFileFault](MiResolvePageFileFault_function_0036D968.md) at `0x0036E7DA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0036A974  48 83 EC 28                     sub rsp, 0x28
0036A978  8B 41 50                        mov eax, dword ptr [rcx + 0x50]
0036A97B  4C 8B CA                        mov r9, rdx
0036A97E  44 8B C0                        mov r8d, eax
0036A981  49 8B C9                        mov rcx, r9
0036A984  41 83 E0 07                     and r8d, 7
0036A988  24 40                           and al, 0x40
0036A98A  F6 D8                           neg al
0036A98C  1B D2                           sbb edx, edx
0036A98E  83 E2 05                        and edx, 5
0036A991  E8 0E 00 00 00                  call 0x14036a9a4
0036A996  48 83 C4 28                     add rsp, 0x28
0036A99A  C3                              ret
0036A99B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSetInPagePrefetchPriority(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 80))))) & (7));
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 80))) & (64));
    result = (unsigned __int8)(-(result));
    a2 = (unsigned int)((a2) & (5));
    result = MiSetInPagePriority(a2, a2, a3, a2);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiSetInPagePrefetchPriority(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    a3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x50))))) & (7));
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x50))) & (64));
    result = (uint8_t)(-(result));
    Arg2 = (uint32_t)((Arg2) & (5));
    result = MiSetInPagePriority(Arg2, Arg2, a3, Arg2);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x50` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0036A974&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0036A974[BB_0036A974]
  bb_0036A99B[BB_0036A99B]
```
