# sub_0094D04A

- RVA: `0x0094D04A`–`0x0094D06F` (길이 `37` bytes)
- VA: `0x000000014094D04A`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009163C`
- 디코드: `8`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0094D051` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0094D04A` → RVA `0x00FD9BA0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0094D051` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0094D056` → [sub_0094CF53 + 0x2B](Unknown_function_0094CF53.md) (`tail-transfer`)
  - `0x0094D06A` → [sub_0094CF53 + 0x3A](Unknown_function_0094CF53.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0094D04A  48 8D 0D 4F CB 68 00            lea rcx, [rip + 0x68cb4f]
0094D051  E8 7A 8D 91 FF                  call 0x140265dd0
0094D056  E9 23 FF FF FF                  jmp 0x14094cf7e
0094D05B  80 49 2C 04                     or byte ptr [rcx + 0x2c], 4
0094D05F  48 8D 41 18                     lea rax, [rcx + 0x18]
0094D063  48 89 40 08                     mov qword ptr [rax + 8], rax
0094D067  48 89 00                        mov qword ptr [rax], rax
0094D06A  E9 1E FF FF FF                  jmp 0x14094cf8d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0094D04A(void)
{
    __int64 result;

    result = ExfTryToWakePushLock(v_rip + 6867791, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_0094D04A(void)
{
    int64_t result;

    result = ExfTryToWakePushLock(v_rip + 6867791, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0094D04A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0094D04A[BB_0094D04A]
  bb_0094D05B[BB_0094D05B]
```
