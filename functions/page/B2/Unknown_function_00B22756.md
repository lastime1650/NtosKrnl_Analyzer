# sub_00B22756

- RVA: `0x00B22756`–`0x00B22776` (길이 `32` bytes)
- VA: `0x0000000140B22756`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008D170`
- 디코드: `8`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B22759` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00B22767` → [AlpcpCancelMessage](../89/AlpcpCancelMessage_function_00894120.md) (function, `0x00894120`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B22759` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B22771` → [AlpcpReceiveSynchronousReply + 0x15B](../92/AlpcpReceiveSynchronousReply_function_009224F0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B22756  48 8B CF                        mov rcx, rdi
00B22759  E8 A2 EE 7B FF                  call 0x1402e1600
00B2275E  45 33 C0                        xor r8d, r8d
00B22761  48 8B D3                        mov rdx, rbx
00B22764  49 8B CD                        mov rcx, r13
00B22767  E8 B4 19 D7 FF                  call 0x140894120
00B2276C  B8 00 07 00 C0                  mov eax, 0xc0000700
00B22771  E9 D5 FE DF FF                  jmp 0x14092264b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B22756(__int64 a1, __int64 a2, int a3)
{
    __int64 result;

    result = KeAbPostRelease(v_rdi, a2, a3, a4);
    a3 = 0;
    result = AlpcpCancelMessage(v_r13, v_rbx, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B22756(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;

    result = KeAbPostRelease(local_rdi, Arg2, Arg3, a4);
    Arg3 = 0;
    result = AlpcpCancelMessage(local_r13, local_rbx, Arg3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B22756&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B22756[BB_00B22756]
```
