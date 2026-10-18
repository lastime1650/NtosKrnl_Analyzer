# VfQueryDriverContext

- RVA: `0x00612910`–`0x0061294A` (길이 `58` bytes)
- VA: `0x0000000140612910`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `18`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00612929` → [ViIsContextIdValid](../../pagevrfy/B9/ViIsContextIdValid_function_00B94934.md) (function, `0x00B94934`)
- `0x0061293B` → [ViQueryObjectContext](../../pagevrfy/B9/ViQueryObjectContext_function_00B9499C.md) (function, `0x00B9499C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00612914` → RVA `0x00F04984` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00612929` → [ViIsContextIdValid](../../pagevrfy/B9/ViIsContextIdValid_function_00B94934.md) (`.text` → `PAGEVRFY`)
  - `0x0061293B` → [ViQueryObjectContext](../../pagevrfy/B9/ViQueryObjectContext_function_00B9499C.md) (`.text` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00612910  48 83 EC 28                     sub rsp, 0x28
00612914  83 3D 69 20 8F 00 00            cmp dword ptr [rip + 0x8f2069], 0
0061291B  4C 8B C9                        mov r9, rcx
0061291E  74 22                           je 0x140612942
00612920  41 BA 01 00 00 00               mov r10d, 1
00612926  41 8B CA                        mov ecx, r10d
00612929  E8 06 20 58 00                  call 0x140b94934
0061292E  84 C0                           test al, al
00612930  74 10                           je 0x140612942
00612932  44 8B C2                        mov r8d, edx
00612935  49 8B C9                        mov rcx, r9
00612938  41 8B D2                        mov edx, r10d
0061293B  E8 5C 20 58 00                  call 0x140b9499c
00612940  EB 02                           jmp 0x140612944
00612942  33 C0                           xor eax, eax
00612944  48 83 C4 28                     add rsp, 0x28
00612948  C3                              ret
00612949  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfQueryDriverContext(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(v_rip + 9379945)) == 0) goto loc_00612942;
    result = ViIsContextIdValid(1, a2, a3, a1);
    if ((unsigned __int8)(result) == 0) goto loc_00612942;
    result = ViQueryObjectContext(a1, 1, (unsigned int)(a2), a1);
    goto loc_00612944;
loc_00612942:
    result = 0;
loc_00612944:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfQueryDriverContext(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(v_rip + 0x8F2069)) == 0) goto loc_00612942;
    result = ViIsContextIdValid(1, Arg2, a3, Arg1);
    if ((uint8_t)(result) == 0) goto loc_00612942;
    result = ViQueryObjectContext(Arg1, 1, (uint32_t)(Arg2), Arg1);
    goto loc_00612944;
loc_00612942:
    result = 0;
loc_00612944:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00612910&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00612910[BB_00612910]
  bb_00612920[BB_00612920]
  bb_00612932[BB_00612932]
  bb_00612942[BB_00612942]
  bb_00612944[BB_00612944]
  bb_00612949[BB_00612949]
  bb_00612910 -->|branch| bb_00612942
  bb_00612910 -->|fallthrough| bb_00612920
  bb_00612920 -->|branch| bb_00612942
  bb_00612920 -->|fallthrough| bb_00612932
  bb_00612932 -->|branch| bb_00612944
  bb_00612942 -->|flow| bb_00612944
```
