# sub_00B49048

- RVA: `0x00B49048`–`0x00B49062` (길이 `26` bytes)
- VA: `0x0000000140B49048`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BA8D0`
- 디코드: `7`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B4904F` → [PiSwCloseDescendants](../A9/PiSwCloseDescendants_function_00A9E564.md) (function, `0x00A9E564`)
- `0x00B49057` → [PiSwCloseDevice](../AA/PiSwCloseDevice_function_00AAB6F4.md) (function, `0x00AAB6F4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B4905D` → [PiSwCloseDescendants + 0x5D](../A9/PiSwCloseDescendants_function_00A9E564.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B49048  48 8D 4E 48                     lea rcx, [rsi + 0x48]
00B4904C  40 8A D5                        mov dl, bpl
00B4904F  E8 10 55 F5 FF                  call 0x140a9e564
00B49054  48 8B CE                        mov rcx, rsi
00B49057  E8 98 26 F6 FF                  call 0x140aab6f4
00B4905C  90                              nop
00B4905D  E9 5F 55 F5 FF                  jmp 0x140a9e5c1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B49048(void)
{
    __int64 result;

    result = PiSwCloseDescendants(v_rsi + 72, (unsigned __int8)(v_rbp), a3, a4);
    result = PiSwCloseDevice(v_rsi, (unsigned __int8)(v_rbp), a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B49048(void)
{
    int64_t result;

    result = PiSwCloseDescendants(local_rsi + 72, (uint8_t)(local_rbp), a3, a4);
    result = PiSwCloseDevice(local_rsi, (uint8_t)(local_rbp), a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B49048&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B49048[BB_00B49048]
```
