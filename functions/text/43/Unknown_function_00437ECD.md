# sub_00437ECD

- RVA: `0x00437ECD`–`0x00437F00` (길이 `51` bytes)
- VA: `0x0000000140437ECD`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A33AC`
- 디코드: `13`개 명령, `51/51` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x00437ED0` → [sub_00437E4E + 0x9](Unknown_function_00437E4E.md) (`tail-transfer`)
  - `0x00437ED6` → [sub_00437E4E + 0x9](Unknown_function_00437E4E.md) (`tail-transfer`)
  - `0x00437EDE` → [sub_00437D03 + 0xB9](Unknown_function_00437D03.md) (`tail-transfer`)
  - `0x00437EE8` → [sub_00437D03 + 0xB9](Unknown_function_00437D03.md) (`tail-transfer`)
  - `0x00437EFB` → [sub_00437E4E + 0x9](Unknown_function_00437E4E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00437ECD  4D 85 F6                        test r14, r14
00437ED0  74 85                           je 0x140437e57
00437ED2  66 44 89 29                     mov word ptr [rcx], r13w
00437ED6  E9 7C FF FF FF                  jmp 0x140437e57
00437EDB  4D 85 C9                        test r9, r9
00437EDE  0F 84 D8 FE FF FF               je 0x140437dbc
00437EE4  66 45 39 2A                     cmp word ptr [r10], r13w
00437EE8  0F 84 CE FE FF FF               je 0x140437dbc
00437EEE  4D 85 FF                        test r15, r15
00437EF1  B8 05 00 00 80                  mov eax, 0x80000005
00437EF6  0F 44 C3                        cmove eax, ebx
00437EF9  8B D8                           mov ebx, eax
00437EFB  E9 57 FF FF FF                  jmp 0x140437e57
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00437ECD(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    *(unsigned __int16 *)(a1) = (unsigned __int16)(v_r13);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00437ECD(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    *(uint16_t *)(arg1) = (uint16_t)(local_r13);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00437ECD&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00437ECD[BB_00437ECD]
  bb_00437ED2[BB_00437ED2]
  bb_00437EDB[BB_00437EDB]
  bb_00437EE4[BB_00437EE4]
  bb_00437EEE[BB_00437EEE]
  bb_00437ECD -->|fallthrough| bb_00437ED2
  bb_00437EDB -->|fallthrough| bb_00437EE4
  bb_00437EE4 -->|fallthrough| bb_00437EEE
```
