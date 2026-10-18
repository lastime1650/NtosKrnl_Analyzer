# sub_00B258BA

- RVA: `0x00B258BA`–`0x00B258D7` (길이 `29` bytes)
- VA: `0x0000000140B258BA`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00090C68`
- 디코드: `8`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B258C3` → [PspAttachProcessToSyscallProvider](../77/PspAttachProcessToSyscallProvider_function_0077E36C.md) (function, `0x0077E36C`)
- `0x00B258CC` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B258CC` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B258D2` → [PspInheritSyscallProvider + 0x2C](../94/PspInheritSyscallProvider_function_00947F68.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B258BA  45 8B C7                        mov r8d, r15d
00B258BD  48 8B D6                        mov rdx, rsi
00B258C0  49 8B CE                        mov rcx, r14
00B258C3  E8 A4 8A C5 FF                  call 0x14077e36c
00B258C8  48 8D 4E 38                     lea rcx, [rsi + 0x38]
00B258CC  E8 AF 45 82 FF                  call 0x140349e80
00B258D1  90                              nop
00B258D2  E9 BD 26 E2 FF                  jmp 0x140947f94
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B258BA(void)
{
    __int64 result;

    result = PspAttachProcessToSyscallProvider(v_r14, v_rsi, (unsigned int)((unsigned int)(v_r15)), a4);
    result = ExReleaseRundownProtection(v_rsi + 56, v_rsi, (unsigned int)((unsigned int)(v_r15)), a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B258BA(void)
{
    int64_t result;

    result = PspAttachProcessToSyscallProvider(local_r14, local_rsi, (uint32_t)((uint32_t)(local_r15)), a4);
    result = ExReleaseRundownProtection(local_rsi + 56, local_rsi, (uint32_t)((uint32_t)(local_r15)), a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B258BA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B258BA[BB_00B258BA]
```
