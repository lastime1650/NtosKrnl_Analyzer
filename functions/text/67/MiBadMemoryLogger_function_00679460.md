# MiBadMemoryLogger

- RVA: `0x00679460`–`0x006794AD` (길이 `77` bytes)
- VA: `0x0000000140679460`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `24`개 명령, `77/77` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00679470` → [IopAllocateErrorLogEntry](../4A/IopAllocateErrorLogEntry_function_004ABF5C.md) (function, `0x004ABF5C`)
- `0x0067949D` → [IoWriteErrorLogEntry](../4B/IoWriteErrorLogEntry_function_004B5B30.md) (function, `0x004B5B30`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00679460  40 53                           push rbx
00679462  48 83 EC 20                     sub rsp, 0x20
00679466  48 8B D9                        mov rbx, rcx
00679469  41 B0 30                        mov r8b, 0x30
0067946C  33 C9                           xor ecx, ecx
0067946E  33 D2                           xor edx, edx
00679470  E8 E7 2A E3 FF                  call 0x1404abf5c
00679475  48 85 C0                        test rax, rax
00679478  74 28                           je 0x1406794a2
0067947A  C7 40 0C 09 07 00 C0            mov dword ptr [rax + 0xc], 0xc0000709
00679481  8B 13                           mov edx, dword ptr [rbx]
00679483  89 50 10                        mov dword ptr [rax + 0x10], edx
00679486  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
0067948A  48 89 50 20                     mov qword ptr [rax + 0x20], rdx
0067948E  8B 4B 08                        mov ecx, dword ptr [rbx + 8]
00679491  89 48 28                        mov dword ptr [rax + 0x28], ecx
00679494  48 8B C8                        mov rcx, rax
00679497  66 C7 40 02 04 00               mov word ptr [rax + 2], 4
0067949D  E8 8E C6 E3 FF                  call 0x1404b5b30
006794A2  F0 FF 4B 04                     lock dec dword ptr [rbx + 4]
006794A6  48 83 C4 20                     add rsp, 0x20
006794AA  5B                              pop rbx
006794AB  C3                              ret
006794AC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiBadMemoryLogger(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = 0;
    a2 = 0;
    result = IopAllocateErrorLogEntry(a1, a2, 48, a4);
    if (result != 0) {
        *(unsigned int *)(result + 12) = 0xC0000709ULL;
        a2 = *(unsigned int *)(a1);
        *(unsigned int *)(result + 16) = a2;
        a2 = *(unsigned __int64 *)(a1 + 16);
        *(unsigned __int64 *)(result + 32) = a2;
        a1 = *(unsigned int *)(a1 + 8);
        *(unsigned int *)(result + 40) = (unsigned int)(a1);
        a1 = result;
        *(unsigned __int16 *)(result + 2) = 4;
        result = IoWriteErrorLogEntry(a1, a2, 48, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiBadMemoryLogger(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = 0;
    Arg2 = 0;
    result = IopAllocateErrorLogEntry(Arg1, Arg2, 48, a4);
    if (result != 0) {
        *(uint32_t *)(result + 0xC) = 0xC0000709ULL;
        Arg2 = *(uint32_t *)(arg1);
        *(uint32_t *)(result + 0x10) = Arg2;
        Arg2 = *(uint64_t *)(arg1 + 0x10);
        *(uint64_t *)(result + 0x20) = Arg2;
        Arg1 = *(uint32_t *)(arg1 + 0x8);
        *(uint32_t *)(result + 0x28) = (uint32_t)(Arg1);
        Arg1 = result;
        *(uint16_t *)(result + 0x2) = 4;
        result = IoWriteErrorLogEntry(Arg1, Arg2, 48, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R/W` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00679460&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00679460[BB_00679460]
  bb_0067947A[BB_0067947A]
  bb_006794A2[BB_006794A2]
  bb_006794AC[BB_006794AC]
  bb_00679460 -->|branch| bb_006794A2
  bb_00679460 -->|fallthrough| bb_0067947A
  bb_0067947A -->|flow| bb_006794A2
```
