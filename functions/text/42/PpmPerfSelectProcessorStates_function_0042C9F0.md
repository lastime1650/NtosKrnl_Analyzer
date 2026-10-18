# PpmPerfSelectProcessorStates

- RVA: `0x0042C9F0`–`0x0042CA0D` (길이 `29` bytes)
- VA: `0x000000014042C9F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A19A0`
- 디코드: `7`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0042C9FA` → RVA `0x00FC6BA8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0042CA0B` → [sub_0042CA64](Unknown_function_0042CA64.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0042C9F0  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0042C9F5  57                              push rdi
0042C9F6  48 83 EC 20                     sub rsp, 0x20
0042C9FA  48 8B 3D A7 A1 B9 00            mov rdi, qword ptr [rip + 0xb9a1a7]
0042CA01  48 8D 35 A0 A1 B9 00            lea rsi, [rip + 0xb9a1a0]
0042CA08  48 3B FE                        cmp rdi, rsi
0042CA0B  74 57                           je 0x14042ca64
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall PpmPerfSelectProcessorStates(void)
{
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
}
```

## 5. (Beta) C Style

```c
void PpmPerfSelectProcessorStates(void)
{
    int64_t local_rsp;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0042C9F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0042C9F0[BB_0042C9F0]
```
