# NtAlertThreadByThreadIdEx

- RVA: `0x009A7730`–`0x009A7748` (길이 `24` bytes)
- VA: `0x00000001409A7730`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009CB6C`
- 디코드: `8`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [NtAlertThreadByThreadId](NtAlertThreadByThreadId_function_009A7710.md) at `0x009A7716`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009A7730  48 8B C4                        mov rax, rsp
009A7733  56                              push rsi
009A7734  57                              push rdi
009A7735  41 56                           push r14
009A7737  41 57                           push r15
009A7739  48 83 EC 48                     sub rsp, 0x48
009A773D  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
009A7746  33 F6                           xor esi, esi
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtAlertThreadByThreadIdEx(void)
{
    __int64 v_rsi;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (72);
    v_rsi = 0;
    return v_rsp;
}
```

## 5. (Beta) C Style

```c
void NtAlertThreadByThreadIdEx(void)
{
    int64_t local_rsi;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (72);
    local_rsi = 0;
    return local_rsp;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A7730&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A7730[BB_009A7730]
```
