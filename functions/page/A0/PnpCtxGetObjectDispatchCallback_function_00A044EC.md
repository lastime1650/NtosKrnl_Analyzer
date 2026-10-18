# PnpCtxGetObjectDispatchCallback

- RVA: `0x00A044EC`–`0x00A04512` (길이 `38` bytes)
- VA: `0x0000000140A044EC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PnpCreateObjectDispatch](../82/PnpCreateObjectDispatch_function_0082C3EC.md) at `0x0082C44A`
- [PnpDeleteObjectDispatch](../82/PnpDeleteObjectDispatch_function_0082C618.md) at `0x0082C66B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A044EC  45 33 C9                        xor r9d, r9d
00A044EF  8D 42 FF                        lea eax, [rdx - 1]
00A044F2  83 F8 0A                        cmp eax, 0xa
00A044F5  77 13                           ja 0x140a0450a
00A044F7  48 63 C2                        movsxd rax, edx
00A044FA  48 8B 8C C1 28 01 00 00         mov rcx, qword ptr [rcx + rax*8 + 0x128]
00A04502  49 89 08                        mov qword ptr [r8], rcx
00A04505  41 8B C1                        mov eax, r9d
00A04508  C3                              ret
00A04509  CC                              int3
00A0450A  41 B9 0D 00 00 C0               mov r9d, 0xc000000d
00A04510  EB F3                           jmp 0x140a04505
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpCtxGetObjectDispatchCallback(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    a4 = 0;
    if (((unsigned int)(a2 - 1)) > 10) goto loc_00A0450A;
    *(unsigned __int64 *)(a3) = *(unsigned __int64 *)(a1 + (int)((unsigned int)(a2)) * 8 + 296);
loc_00A04505:
    return 0;
loc_00A0450A:
    goto loc_00A04505;
}
```

## 5. (Beta) C Style

```c
int64_t PnpCtxGetObjectDispatchCallback(void *Arg1, void *Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    Arg4 = 0;
    if (((uint32_t)(Arg2 - 1)) > 10) goto loc_00A0450A;
    *(uint64_t *)(arg3) = *(uint64_t *)(arg1 + (int32_t)((uint32_t)(arg2)) * 8 + 0x128);
loc_00A04505:
    return 0;
loc_00A0450A:
    goto loc_00A04505;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x128 + rax*8` | `64` | `R` |
| `Arg2` | `- 0x1` | `32` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A044EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A044EC[BB_00A044EC]
  bb_00A044F7[BB_00A044F7]
  bb_00A04505[BB_00A04505]
  bb_00A04509[BB_00A04509]
  bb_00A0450A[BB_00A0450A]
  bb_00A044EC -->|branch| bb_00A0450A
  bb_00A044EC -->|fallthrough| bb_00A044F7
  bb_00A044F7 -->|flow| bb_00A04505
  bb_00A04509 -->|flow| bb_00A0450A
  bb_00A0450A -->|branch| bb_00A04505
```
