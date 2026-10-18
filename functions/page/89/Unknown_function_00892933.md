# sub_00892933

- RVA: `0x00892933`–`0x0089294B` (길이 `24` bytes)
- VA: `0x0000000140892933`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007DC60`
- 디코드: `5`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00892941` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0089293A` → RVA `0x00F10080` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00892941` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00892946` → [sub_008926FB + 0x1AB](Unknown_function_008926FB.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00892933  B9 03 00 00 00                  mov ecx, 3
00892938  CD 29                           int 0x29
0089293A  48 8D 0D 3F D7 67 00            lea rcx, [rip + 0x67d73f]
00892941  E8 8A 34 9D FF                  call 0x140265dd0
00892946  E9 5B FF FF FF                  jmp 0x1408928a6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00892933(void)
{
    __int64 result;

    result = ExfTryToWakePushLock(v_rip + 6805311, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00892933(void)
{
    int64_t result;

    result = ExfTryToWakePushLock(v_rip + 6805311, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00892933&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00892933[BB_00892933]
```
