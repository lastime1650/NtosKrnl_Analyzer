# sub_00855CB3

- RVA: `0x00855CB3`–`0x00855CCB` (길이 `24` bytes)
- VA: `0x0000000140855CB3`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006A298`
- 디코드: `6`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00855CC1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00855CC1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00855CC6` → [sub_00855A5C + 0xF9](Unknown_function_00855A5C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00855CB3  44 0F B7 C6                     movzx r8d, si
00855CB7  48 83 C2 4C                     add rdx, 0x4c
00855CBB  4D 03 C0                        add r8, r8
00855CBE  49 8B C9                        mov rcx, r9
00855CC1  E8 7A 0B E7 FF                  call 0x1406c6840
00855CC6  E9 8A FE FF FF                  jmp 0x140855b55
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00855CB3(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;

    a2 = (a2) + (76);
    a3 = ((unsigned __int16)(v_rsi)) + ((unsigned __int16)(v_rsi));
    result = memcpy(a4, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00855CB3(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;

    Arg2 = (Arg2) + (76);
    Arg3 = ((uint16_t)(local_rsi)) + ((uint16_t)(local_rsi));
    result = memcpy(Arg4, Arg2, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00855CB3&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00855CB3[BB_00855CB3]
```
