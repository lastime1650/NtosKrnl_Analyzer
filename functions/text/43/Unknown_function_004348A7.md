# sub_004348A7

- RVA: `0x004348A7`–`0x004348BE` (길이 `23` bytes)
- VA: `0x00000001404348A7`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A2A28`
- 디코드: `6`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004348B4` → [ExpWaitForSpinLockSharedAndAcquire](../36/ExpWaitForSpinLockSharedAndAcquire_function_00362380.md) (function, `0x00362380`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x004348A9` → [sub_004346AE + 0x6A](Unknown_function_004346AE.md) (`tail-transfer`)
  - `0x004348B9` → [sub_004346AE + 0x58](Unknown_function_004346AE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
004348A7  85 C0                           test eax, eax
004348A9  0F 89 69 FE FF FF               jns 0x140434718
004348AF  B2 FF                           mov dl, 0xff
004348B1  49 8B CF                        mov rcx, r15
004348B4  E8 C7 DA F2 FF                  call 0x140362380
004348B9  E9 48 FE FF FF                  jmp 0x140434706
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_004348A7(void)
{
    __int64 result;

    result = ExpWaitForSpinLockSharedAndAcquire(v_r15, 255, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_004348A7(void)
{
    int64_t result;

    result = ExpWaitForSpinLockSharedAndAcquire(local_r15, 255, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004348A7&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004348A7[BB_004348A7]
  bb_004348AF[BB_004348AF]
  bb_004348A7 -->|fallthrough| bb_004348AF
```
