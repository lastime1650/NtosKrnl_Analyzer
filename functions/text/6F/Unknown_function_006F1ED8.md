# sub_006F1ED8

- RVA: `0x006F1ED8`–`0x006F1EF0` (길이 `24` bytes)
- VA: `0x00000001406F1ED8`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9134`
- 디코드: `7`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006F1EE5` → [IopFreeIrpExtension](../24/IopFreeIrpExtension_function_0024EDB0.md) (function, `0x0024EDB0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006F1EEB` → [IoSetActivityIdIrp + 0x4D](../45/IoSetActivityIdIrp_function_0045B220.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F1ED8  BF BB 00 00 C0                  mov edi, 0xc00000bb
006F1EDD  44 8A C5                        mov r8b, bpl
006F1EE0  33 D2                           xor edx, edx
006F1EE2  48 8B CB                        mov rcx, rbx
006F1EE5  E8 C6 CE B5 FF                  call 0x14024edb0
006F1EEA  90                              nop
006F1EEB  E9 7D 93 D6 FF                  jmp 0x14045b26d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F1ED8(__int64 a1, int a2)
{
    __int64 result;

    a2 = 0;
    result = IopFreeIrpExtension(v_rbx, a2, (unsigned __int8)(v_rbp), a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006F1ED8(int64_t Arg1, int32_t Arg2)
{
    int64_t result;

    Arg2 = 0;
    result = IopFreeIrpExtension(local_rbx, Arg2, (uint8_t)(local_rbp), a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F1ED8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F1ED8[BB_006F1ED8]
```
