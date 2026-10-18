# PopCompressCallback

- RVA: `0x00B6CD50`–`0x00B6CD6C` (길이 `28` bytes)
- VA: `0x0000000140B6CD50`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B6CD61` → [PopRequestWrite](PopRequestWrite_function_00B6EB14.md) (function, `0x00B6EB14`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B6CD54` → RVA `0x00F0BFC8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B6CD50  48 83 EC 28                     sub rsp, 0x28
00B6CD54  48 8B 15 6D F2 39 00            mov rdx, qword ptr [rip + 0x39f26d]
00B6CD5B  41 B8 01 00 00 00               mov r8d, 1
00B6CD61  E8 AE 1D 00 00                  call 0x140b6eb14
00B6CD66  48 83 C4 28                     add rsp, 0x28
00B6CD6A  C3                              ret
00B6CD6B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopCompressCallback(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PopRequestWrite(a1, *(unsigned __int64 *)(v_rip + 3797613), 1, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PopCompressCallback(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PopRequestWrite(a1, *(uint64_t *)(v_rip + 0x39F26D), 1, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B6CD50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B6CD50[BB_00B6CD50]
  bb_00B6CD6B[BB_00B6CD6B]
```
