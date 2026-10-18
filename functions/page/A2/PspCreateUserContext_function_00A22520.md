# PspCreateUserContext

- RVA: `0x00A22520`–`0x00A2257C` (길이 `92` bytes)
- VA: `0x0000000140A22520`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `18`개 명령, `92/92` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEB341`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A22520  F6 C2 01                        test dl, 1
00A22523  75 07                           jne 0x140a2252c
00A22525  C7 41 30 0B 00 10 00            mov dword ptr [rcx + 0x30], 0x10000b
00A2252C  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
00A22531  BA 2B 00 00 00                  mov edx, 0x2b
00A22536  66 89 51 42                     mov word ptr [rcx + 0x42], dx
00A2253A  BA 80 1F 00 00                  mov edx, 0x1f80
00A2253F  89 51 34                        mov dword ptr [rcx + 0x34], edx
00A22542  89 91 18 01 00 00               mov dword ptr [rcx + 0x118], edx
00A22548  4C 89 81 F8 00 00 00            mov qword ptr [rcx + 0xf8], r8
00A2254F  4C 89 89 80 00 00 00            mov qword ptr [rcx + 0x80], r9
00A22556  48 89 81 88 00 00 00            mov qword ptr [rcx + 0x88], rax
00A2255D  C7 41 3A 2B 00 2B 00            mov dword ptr [rcx + 0x3a], 0x2b002b
00A22564  C7 41 3E 53 00 2B 00            mov dword ptr [rcx + 0x3e], 0x2b0053
00A2256B  66 C7 41 38 33 00               mov word ptr [rcx + 0x38], 0x33
00A22571  66 C7 81 00 01 00 00 7F 02      mov word ptr [rcx + 0x100], 0x27f
00A2257A  C3                              ret
00A2257B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspCreateUserContext(__int64 a1, unsigned __int8 a2, __int64 a3, __int64 a4, __int64 a5)
{
    if (((a2) & (1)) == 0) {
        *(unsigned int *)(a1 + 48) = 0x10000BULL;
    }
    *(unsigned __int16 *)(a1 + 66) = 43;
    *(unsigned int *)(a1 + 52) = (unsigned int)((unsigned int)(0x1F80ULL));
    *(unsigned int *)(a1 + 280) = (unsigned int)((unsigned int)(0x1F80ULL));
    *(unsigned __int64 *)(a1 + 248) = a3;
    *(unsigned __int64 *)(a1 + 128) = a4;
    *(unsigned __int64 *)(a1 + 136) = a5;
    *(unsigned int *)(a1 + 58) = 0x2B002BULL;
    *(unsigned int *)(a1 + 62) = 0x2B0053ULL;
    *(unsigned __int16 *)(a1 + 56) = 51;
    *(unsigned __int16 *)(a1 + 256) = 639;
    return a5;
}
```

## 5. (Beta) C Style

```c
int64_t PspCreateUserContext(void *Arg1, uint8_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if (((Arg2) & (1)) == 0) {
        *(uint32_t *)(arg1 + 0x30) = 0x10000BULL;
    }
    *(uint16_t *)(arg1 + 0x42) = 43;
    *(uint32_t *)(arg1 + 0x34) = (uint32_t)((uint32_t)(0x1F80ULL));
    *(uint32_t *)(arg1 + 0x118) = (uint32_t)((uint32_t)(0x1F80ULL));
    *(uint64_t *)(arg1 + 0xF8) = Arg3;
    *(uint64_t *)(arg1 + 0x80) = Arg4;
    *(uint64_t *)(arg1 + 0x88) = Arg5;
    *(uint32_t *)(arg1 + 0x3A) = 0x2B002BULL;
    *(uint32_t *)(arg1 + 0x3E) = 0x2B0053ULL;
    *(uint16_t *)(arg1 + 0x38) = 51;
    *(uint16_t *)(arg1 + 0x100) = 639;
    return Arg5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `32` | `W` |
| `Arg1` | `+ 0x34` | `32` | `W` |
| `Arg1` | `+ 0x38` | `16` | `W` |
| `Arg1` | `+ 0x3A` | `32` | `W` |
| `Arg1` | `+ 0x3E` | `32` | `W` |
| `Arg1` | `+ 0x42` | `16` | `W` |
| `Arg1` | `+ 0x80` | `64` | `W` |
| `Arg1` | `+ 0x88` | `64` | `W` |
| `Arg1` | `+ 0xF8` | `64` | `W` |
| `Arg1` | `+ 0x100` | `16` | `W` |
| `Arg1` | `+ 0x118` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A22520&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A22520[BB_00A22520]
  bb_00A22525[BB_00A22525]
  bb_00A2252C[BB_00A2252C]
  bb_00A2257B[BB_00A2257B]
  bb_00A22520 -->|branch| bb_00A2252C
  bb_00A22520 -->|fallthrough| bb_00A22525
  bb_00A22525 -->|flow| bb_00A2252C
```
