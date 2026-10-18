# sub_002F8270

- RVA: `0x002F8270`–`0x002F828E` (길이 `30` bytes)
- VA: `0x00000001402F8270`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000725A0`
- 디코드: `6`개 명령, `30/30` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x002F8276` → [sub_002F80EA + 0x6A](Unknown_function_002F80EA.md) (`tail-transfer`)
  - `0x002F827F` → [sub_002F80EA + 0x6A](Unknown_function_002F80EA.md) (`tail-transfer`)
  - `0x002F8289` → [sub_002F80EA + 0x93](Unknown_function_002F80EA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002F8270  81 F9 00 60 00 00               cmp ecx, 0x6000
002F8276  0F 82 D8 FE FF FF               jb 0x1402f8154
002F827C  83 CD 05                        or ebp, 5
002F827F  E9 D0 FE FF FF                  jmp 0x1402f8154
002F8284  B8 F2 00 00 C0                  mov eax, 0xc00000f2
002F8289  E9 EF FE FF FF                  jmp 0x1402f817d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002F8270(int a1)
{
    __int64 v_rbp;

    v_rbp = (unsigned int)((v_rbp) | (5));
}
```

## 5. (Beta) C Style

```c
int64_t sub_002F8270(int32_t Arg1)
{
    int64_t local_rbp;

    local_rbp = (uint32_t)((local_rbp) | (5));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F8270&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002F8270[BB_002F8270]
  bb_002F827C[BB_002F827C]
  bb_002F8284[BB_002F8284]
  bb_002F8270 -->|fallthrough| bb_002F827C
```
