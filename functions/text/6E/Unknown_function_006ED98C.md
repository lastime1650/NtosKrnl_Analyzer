# sub_006ED98C

- RVA: `0x006ED98C`–`0x006ED9A2` (길이 `22` bytes)
- VA: `0x00000001406ED98C`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009FEB4`
- 디코드: `5`개 명령, `22/22` bytes 표시
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
- `0x006ED991` → RVA `0x00F05C48` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006ED99B` → [sub_006ED9D8](Unknown_function_006ED9D8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006ED98C  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
006ED991  48 8B 35 B0 82 81 00            mov rsi, qword ptr [rip + 0x8182b0]
006ED998  48 85 F6                        test rsi, rsi
006ED99B  74 3B                           je 0x1406ed9d8
006ED99D  BA 01 00 00 00                  mov edx, 1
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_006ED98C(void)
{
    unsigned __int64 v_stack_p38;

    v_stack_p38 = v_rsi;
    return;
}
```

## 5. (Beta) C Style

```c
void sub_006ED98C(void)
{
    uint64_t v_stack_p38;

    v_stack_p38 = local_rsi;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006ED98C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006ED98C[BB_006ED98C]
  bb_006ED99D[BB_006ED99D]
  bb_006ED98C -->|fallthrough| bb_006ED99D
```
