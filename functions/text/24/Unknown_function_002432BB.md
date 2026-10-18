# sub_002432BB

- RVA: `0x002432BB`–`0x002432E7` (길이 `44` bytes)
- VA: `0x00000001402432BB`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00061A7C`
- 디코드: `6`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002432DA` → [sub_002434F4](Unknown_function_002434F4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002432BB  4C 89 B4 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], r14
002432C3  48 BD F8 FF FF FF 7F 00 00 00   movabs rbp, 0x7ffffffff8
002432CD  48 BE 00 00 00 00 80 F6 FF FF   movabs rsi, 0xfffff68000000000
002432D7  83 F9 02                        cmp ecx, 2
002432DA  0F 84 14 02 00 00               je 0x1402434f4
002432E0  83 BB 98 00 00 00 00            cmp dword ptr [rbx + 0x98], 0
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_002432BB(int a1)
{
    unsigned __int64 v_stack_pF8;

    v_stack_pF8 = v_r14;
    return;
}
```

## 5. (Beta) C Style

```c
void sub_002432BB(int32_t Arg1)
{
    uint64_t v_stack_pF8;

    v_stack_pF8 = local_r14;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002432BB&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002432BB[BB_002432BB]
  bb_002432E0[BB_002432E0]
  bb_002432BB -->|fallthrough| bb_002432E0
```
