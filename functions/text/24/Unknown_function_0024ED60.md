# sub_0024ED60

- RVA: `0x0024ED60`–`0x0024EDAA` (길이 `74` bytes)
- VA: `0x000000014024ED60`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063298`
- 디코드: `17`개 명령, `74/74` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0024ED63` → [ExIsSpecialPoolAddress](../49/ExIsSpecialPoolAddress_function_0049C410.md) (function, `0x0049C410`)
- `0x0024ED8C` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x0024ED6A` → [sub_0024E7EF + 0x35](Unknown_function_0024E7EF.md) (`tail-transfer`)
  - `0x0024ED70` → [sub_0024E7EF + 0x209](Unknown_function_0024E7EF.md) (`tail-transfer`)
  - `0x0024ED78` → [sub_0024EAB1 + 0x127](Unknown_function_0024EAB1.md) (`tail-transfer`)
  - `0x0024ED83` → [sub_0024EAB1 + 0xAD](Unknown_function_0024EAB1.md) (`tail-transfer`)
  - `0x0024ED91` → [sub_0024E7EF + 0x209](Unknown_function_0024E7EF.md) (`tail-transfer`)
  - `0x0024ED99` → [sub_0024E7EF + 0x66](Unknown_function_0024E7EF.md) (`tail-transfer`)
  - `0x0024EDA5` → [sub_0024E7EF + 0x6C](Unknown_function_0024E7EF.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0024ED60  48 8B CB                        mov rcx, rbx
0024ED63  E8 A8 D6 24 00                  call 0x14049c410
0024ED68  85 C0                           test eax, eax
0024ED6A  0F 84 B4 FA FF FF               je 0x14024e824
0024ED70  E9 83 FC FF FF                  jmp 0x14024e9f8
0024ED75  49 8B F7                        mov rsi, r15
0024ED78  E9 5B FE FF FF                  jmp 0x14024ebd8
0024ED7D  45 8B CE                        mov r9d, r14d
0024ED80  41 8B F6                        mov esi, r14d
0024ED83  E9 D6 FD FF FF                  jmp 0x14024eb5e
0024ED88  48 8D 4E D0                     lea rcx, [rsi - 0x30]
0024ED8C  E8 03 36 15 00                  call 0x1403a2394
0024ED91  E9 62 FC FF FF                  jmp 0x14024e9f8
0024ED96  80 F9 04                        cmp cl, 4
0024ED99  0F 84 B6 FA FF FF               je 0x14024e855
0024ED9F  41 BD 00 01 00 00               mov r13d, 0x100
0024EDA5  E9 B1 FA FF FF                  jmp 0x14024e85b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0024ED60(void)
{
    __int64 result;

    result = ExIsSpecialPoolAddress(v_rbx, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_0024ED60(void)
{
    int64_t result;

    result = ExIsSpecialPoolAddress(local_rbx, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0024ED60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0024ED60[BB_0024ED60]
  bb_0024ED70[BB_0024ED70]
  bb_0024ED75[BB_0024ED75]
  bb_0024ED7D[BB_0024ED7D]
  bb_0024ED88[BB_0024ED88]
  bb_0024ED96[BB_0024ED96]
  bb_0024ED9F[BB_0024ED9F]
  bb_0024ED60 -->|fallthrough| bb_0024ED70
  bb_0024ED96 -->|fallthrough| bb_0024ED9F
```
