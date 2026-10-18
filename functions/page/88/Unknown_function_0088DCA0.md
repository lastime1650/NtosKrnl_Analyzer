# sub_0088DCA0

- RVA: `0x0088DCA0`–`0x0088DCBA` (길이 `26` bytes)
- VA: `0x000000014088DCA0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007D4CC`
- 디코드: `6`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0088DCA3` → [AlpcpLogSendMessage](../89/AlpcpLogSendMessage_function_008903B4.md) (function, `0x008903B4`)
- `0x0088DCB0` → [AlpcpLogWaitForReply](../74/AlpcpLogWaitForReply_function_0074D390.md) (function, `0x0074D390`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0088DCA8` → [sub_0088DAFD](Unknown_function_0088DAFD.md) (`tail-transfer`)
  - `0x0088DCB5` → [sub_0088DAFD + 0xC0](Unknown_function_0088DAFD.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0088DCA0  48 8B CF                        mov rcx, rdi
0088DCA3  E8 0C 27 00 00                  call 0x1408903b4
0088DCA8  E9 50 FE FF FF                  jmp 0x14088dafd
0088DCAD  48 8B CF                        mov rcx, rdi
0088DCB0  E8 DB F6 EB FF                  call 0x14074d390
0088DCB5  E9 03 FF FF FF                  jmp 0x14088dbbd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0088DCA0(void)
{
    __int64 result;

    result = AlpcpLogSendMessage(v_rdi, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_0088DCA0(void)
{
    int64_t result;

    result = AlpcpLogSendMessage(local_rdi, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0088DCA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0088DCA0[BB_0088DCA0]
  bb_0088DCAD[BB_0088DCAD]
```
