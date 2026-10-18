# ExpBoostIoAfterAcquire

- RVA: `0x00215CE0`–`0x00215D0E` (길이 `46` bytes)
- VA: `0x0000000140215CE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005E208`
- 디코드: `15`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ExpAcquireSharedStarveExclusive](../34/ExpAcquireSharedStarveExclusive_function_003411C0.md) at `0x00341680`
- [sub_006E96C4](../6E/Unknown_function_006E96C4.md) at `0x006E97B2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00215D08` → [sub_00215EF4](Unknown_function_00215EF4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00215CE0  4C 8B DC                        mov r11, rsp
00215CE3  55                              push rbp
00215CE4  56                              push rsi
00215CE5  41 57                           push r15
00215CE7  48 83 EC 50                     sub rsp, 0x50
00215CEB  33 C0                           xor eax, eax
00215CED  45 8B F8                        mov r15d, r8d
00215CF0  0F 57 C0                        xorps xmm0, xmm0
00215CF3  48 8B F2                        mov rsi, rdx
00215CF6  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00215CFB  49 89 43 C8                     mov qword ptr [r11 - 0x38], rax
00215CFF  48 8B E9                        mov rbp, rcx
00215D02  0F B7 41 1A                     movzx eax, word ptr [rcx + 0x1a]
00215D06  A8 08                           test al, 8
00215D08  0F 85 E6 01 00 00               jne 0x140215ef4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpBoostIoAfterAcquire(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;

    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m48 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 56) = 0;
}
```

## 5. (Beta) C Style

```c
int64_t ExpBoostIoAfterAcquire(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m48;

    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m48 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x38) = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1A` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00215CE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00215CE0[BB_00215CE0]
```
