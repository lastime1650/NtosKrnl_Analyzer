# MiUnmapSinglePage

- RVA: `0x004D4B00`–`0x004D4B3A` (길이 `58` bytes)
- VA: `0x00000001404D4B00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004D4B2F` → [MiReleasePtes](../24/MiReleasePtes_function_00247240.md) (function, `0x00247240`)

### Direct callers
- [MiFreeForkMappingPte](../../page/70/MiFreeForkMappingPte_function_00705848.md) at `0x00705858`

### Static image references
- `0x004D4B22` → RVA `0x00E37668` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004D4B00  48 83 EC 28                     sub rsp, 0x28
004D4B04  48 C1 E9 09                     shr rcx, 9
004D4B08  48 BA F8 FF FF FF 7F 00 00 00   movabs rdx, 0x7ffffffff8
004D4B12  48 23 D1                        and rdx, rcx
004D4B15  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
004D4B1F  48 03 D0                        add rdx, rax
004D4B22  48 8D 0D 3F 2B 96 00            lea rcx, [rip + 0x962b3f]
004D4B29  41 B8 01 00 00 00               mov r8d, 1
004D4B2F  E8 0C 27 D7 FF                  call 0x140247240
004D4B34  48 83 C4 28                     add rsp, 0x28
004D4B38  C3                              ret
004D4B39  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUnmapSinglePage(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (a1) >> (9);
    a2 = (a2) & (a1);
    a2 = (a2) + (result);
    result = MiReleasePtes(v_rip + 9841471, a2, 1, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiUnmapSinglePage(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (Arg1) >> (9);
    a2 = (a2) & (Arg1);
    a2 = (a2) + (result);
    result = MiReleasePtes(v_rip + 9841471, a2, 1, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004D4B00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004D4B00[BB_004D4B00]
  bb_004D4B39[BB_004D4B39]
```
