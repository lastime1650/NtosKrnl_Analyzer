# sub_00397C33

- RVA: `0x00397C33`–`0x00397C4F` (길이 `28` bytes)
- VA: `0x0000000140397C33`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00081424`
- 디코드: `7`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00397C36` → [KeIsThreadRunning](KeIsThreadRunning_function_00396720.md) (function, `0x00396720`)
- `0x00397C45` → [EtwTraceEnqueueWork](EtwTraceEnqueueWork_function_0039674C.md) (function, `0x0039674C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00397C4A` → [KeInsertQueueEx + 0x68](KeInsertQueueEx_function_00397910.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00397C33  48 8B CB                        mov rcx, rbx
00397C36  E8 E5 EA FF FF                  call 0x140396720
00397C3B  44 0F B6 C0                     movzx r8d, al
00397C3F  48 8B CB                        mov rcx, rbx
00397C42  48 8B D6                        mov rdx, rsi
00397C45  E8 02 EB FF FF                  call 0x14039674c
00397C4A  E9 29 FD FF FF                  jmp 0x140397978
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00397C33(void)
{
    __int64 result;

    result = KeIsThreadRunning(v_rbx, a2, a3, a4);
    result = EtwTraceEnqueueWork(v_rbx, v_rsi, (unsigned __int8)(result), a4);
}
```

## 5. (Beta) C Style

```c
void sub_00397C33(void)
{
    int64_t result;

    result = KeIsThreadRunning(local_rbx, a2, a3, a4);
    result = EtwTraceEnqueueWork(local_rbx, local_rsi, (uint8_t)(result), a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00397C33&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00397C33[BB_00397C33]
```
