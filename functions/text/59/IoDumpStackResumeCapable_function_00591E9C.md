# IoDumpStackResumeCapable

- RVA: `0x00591E9C`–`0x00591EC5` (길이 `41` bytes)
- VA: `0x0000000140591E9C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00591EBA` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PopSaveHiberContext](../../pagelk/B6/PopSaveHiberContext_function_00B6F050.md) at `0x00B6F1E7`

### Static image references
- `0x00591EA2` → RVA `0x00E66058` (`.data`; read)
- `0x00591EAB` → RVA `0x00E66018` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00591E9C  48 83 EC 28                     sub rsp, 0x28
00591EA0  33 C0                           xor eax, eax
00591EA2  48 39 05 AF 41 8D 00            cmp qword ptr [rip + 0x8d41af], rax
00591EA9  74 14                           je 0x140591ebf
00591EAB  48 8B 15 66 41 8D 00            mov rdx, qword ptr [rip + 0x8d4166]
00591EB2  48 85 D2                        test rdx, rdx
00591EB5  74 08                           je 0x140591ebf
00591EB7  48 8B C2                        mov rax, rdx
00591EBA  E8 11 8C 12 00                  call 0x1406baad0
00591EBF  48 83 C4 28                     add rsp, 0x28
00591EC3  C3                              ret
00591EC4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoDumpStackResumeCapable(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if ((*(unsigned __int64 *)(v_rip + 9257391)) == 0) goto loc_00591EBF;
    if (*(unsigned __int64 *)(v_rip + 9257318) != 0) {
        result = *(unsigned __int64 *)(v_rip + 9257318);
        result = guard_dispatch_icall(a1, *(unsigned __int64 *)(v_rip + 9257318), a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void IoDumpStackResumeCapable(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if ((*(uint64_t *)(v_rip + 0x8D41AF)) == 0) goto loc_00591EBF;
    if (*(uint64_t *)(v_rip + 0x8D4166) != 0) {
        result = *(uint64_t *)(v_rip + 0x8D4166);
        result = guard_dispatch_icall(a1, *(uint64_t *)(v_rip + 0x8D4166), a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00591E9C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00591E9C[BB_00591E9C]
  bb_00591EAB[BB_00591EAB]
  bb_00591EB7[BB_00591EB7]
  bb_00591EBF[BB_00591EBF]
  bb_00591EC4[BB_00591EC4]
  bb_00591E9C -->|branch| bb_00591EBF
  bb_00591E9C -->|fallthrough| bb_00591EAB
  bb_00591EAB -->|branch| bb_00591EBF
  bb_00591EAB -->|fallthrough| bb_00591EB7
  bb_00591EB7 -->|flow| bb_00591EBF
```
