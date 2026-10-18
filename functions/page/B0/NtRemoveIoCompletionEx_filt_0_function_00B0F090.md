# NtRemoveIoCompletionEx$filt$0

- RVA: `0x00B0F090`–`0x00B0F0C6` (길이 `54` bytes)
- VA: `0x0000000140B0F090`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00086A88`
- 디코드: `16`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B0F090  40 55                           push rbp
00B0F092  48 83 EC 40                     sub rsp, 0x40
00B0F096  48 8B EA                        mov rbp, rdx
00B0F099  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B0F0A2  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00B0F0A6  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
00B0F0AA  0F B6 88 32 02 00 00            movzx ecx, byte ptr [rax + 0x232]
00B0F0B1  88 4D 40                        mov byte ptr [rbp + 0x40], cl
00B0F0B4  0F B6 4D 40                     movzx ecx, byte ptr [rbp + 0x40]
00B0F0B8  33 C0                           xor eax, eax
00B0F0BA  84 C9                           test cl, cl
00B0F0BC  0F 95 C0                        setne al
00B0F0BF  48 83 C4 40                     add rsp, 0x40
00B0F0C3  5D                              pop rbp
00B0F0C4  C3                              ret
00B0F0C5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtRemoveIoCompletionEx_filt_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(a2 + 96) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int8 *)(a2 + 64) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 96) + 562));
    result = 0;
    result = ((unsigned __int8)(*(unsigned __int8 *)(a2 + 64)) != 0) ? 1 : 0;
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtRemoveIoCompletionEx_filt_0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(arg2 + 0x60) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint8_t *)(arg2 + 0x40) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x60) + 0x232));
    result = 0;
    result = ((uint8_t)(*(uint8_t *)(arg2 + 0x40)) != 0) ? 1 : 0;
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x40` | `8` | `R` |
| `Arg2` | `+ 0x40` | `8` | `W` |
| `Arg2` | `+ 0x60` | `64` | `R` |
| `Arg2` | `+ 0x60` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B0F090&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B0F090[BB_00B0F090]
  bb_00B0F0C5[BB_00B0F0C5]
```
