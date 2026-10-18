# SLQueryLicenseValueInternal$filt$1

- RVA: `0x00B150B1`–`0x00B150ED` (길이 `60` bytes)
- VA: `0x0000000140B150B1`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000BF784`
- 디코드: `17`개 명령, `60/60` bytes 표시
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
00B150B1  40 55                           push rbp
00B150B3  48 83 EC 60                     sub rsp, 0x60
00B150B7  48 8B EA                        mov rbp, rdx
00B150BA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B150C3  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
00B150CA  48 8B 85 00 01 00 00            mov rax, qword ptr [rbp + 0x100]
00B150D1  8A 88 32 02 00 00               mov cl, byte ptr [rax + 0x232]
00B150D7  88 4D 6A                        mov byte ptr [rbp + 0x6a], cl
00B150DA  8A 45 6A                        mov al, byte ptr [rbp + 0x6a]
00B150DD  33 C9                           xor ecx, ecx
00B150DF  84 C0                           test al, al
00B150E1  0F 95 C1                        setne cl
00B150E4  8B C1                           mov eax, ecx
00B150E6  48 83 C4 60                     add rsp, 0x60
00B150EA  5D                              pop rbp
00B150EB  C3                              ret
00B150EC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SLQueryLicenseValueInternal_filt_1(__int64 a1, __int64 a2)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (96);
    *(unsigned __int64 *)(a2 + 256) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int8 *)(a2 + 106) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 256) + 562));
    a1 = 0;
    a1 = ((unsigned __int8)(*(unsigned __int8 *)(a2 + 106)) != 0) ? 1 : 0;
    v_rsp = (v_rsp) + (96);
    return (unsigned int)((unsigned int)(a1));
}
```

## 5. (Beta) C Style

```c
int64_t SLQueryLicenseValueInternal_filt_1(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (96);
    *(uint64_t *)(arg2 + 0x100) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint8_t *)(arg2 + 0x6A) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x100) + 0x232));
    Arg1 = 0;
    Arg1 = ((uint8_t)(*(uint8_t *)(arg2 + 0x6A)) != 0) ? 1 : 0;
    local_rsp = (local_rsp) + (96);
    return (uint32_t)((uint32_t)(Arg1));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x6A` | `8` | `R` |
| `Arg2` | `+ 0x6A` | `8` | `W` |
| `Arg2` | `+ 0x100` | `64` | `R` |
| `Arg2` | `+ 0x100` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B150B1&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B150B1[BB_00B150B1]
  bb_00B150EC[BB_00B150EC]
```
