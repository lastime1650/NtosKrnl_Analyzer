# sub_006E1FAC

- RVA: `0x006E1FAC`–`0x006E1FEC` (길이 `64` bytes)
- VA: `0x00000001406E1FAC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076A1C`
- 디코드: `13`개 명령, `64/64` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006E1FD6` → [MiPageFreeToZero + 0x11C](../33/MiPageFreeToZero_function_00337A30.md) (`tail-transfer`)
  - `0x006E1FE7` → [MiPageFreeToZero + 0x11C](../33/MiPageFreeToZero_function_00337A30.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E1FAC  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
006E1FB4  48 8B CB                        mov rcx, rbx
006E1FB7  48 C1 E9 12                     shr rcx, 0x12
006E1FBB  83 E1 03                        and ecx, 3
006E1FBE  0F B6 D3                        movzx edx, bl
006E1FC1  8B 80 50 42 00 00               mov eax, dword ptr [rax + 0x4250]
006E1FC7  C1 E0 02                        shl eax, 2
006E1FCA  49 8B 8C CC 00 14 00 00         mov rcx, qword ptr [r12 + rcx*8 + 0x1400]
006E1FD2  48 39 04 D1                     cmp qword ptr [rcx + rdx*8], rax
006E1FD6  0F 82 70 5B C5 FF               jb 0x140337b4c
006E1FDC  48 0F BA EF 07                  bts rdi, 7
006E1FE1  41 BE 01 04 00 00               mov r14d, 0x401
006E1FE7  E9 60 5B C5 FF                  jmp 0x140337b4c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E1FAC(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17)
{
    __int64 result;

    a1 = (v_rbx) >> (18);
    a1 = (unsigned int)((a1) & (3));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a17 + 16976))) << (2));
}
```

## 5. (Beta) C Style

```c
int64_t sub_006E1FAC(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, void *Arg17)
{
    uint8_t *arg17 = (uint8_t *)Arg17;

    int64_t result;

    Arg1 = (local_rbx) >> (18);
    Arg1 = (uint32_t)((Arg1) & (3));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg17 + 0x4250))) << (2));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg17` | `+ 0x4250` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E1FAC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E1FAC[BB_006E1FAC]
  bb_006E1FDC[BB_006E1FDC]
  bb_006E1FAC -->|fallthrough| bb_006E1FDC
```
