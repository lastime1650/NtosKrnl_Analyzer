# Mi4KStartForSubsection

- RVA: `0x0046C358`–`0x0046C37D` (길이 `37` bytes)
- VA: `0x000000014046C358`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiExtendSection](../../page/98/MiExtendSection_function_00982FDC.md) at `0x009831C8`
- [MiCreateDataFileMap](../../page/98/MiCreateDataFileMap_function_00983494.md) at `0x009836A3`
- [MiCreatePagingFileMap](../../page/98/MiCreatePagingFileMap_function_009852F8.md) at `0x009857D9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0046C358  89 51 24                        mov dword ptr [rcx + 0x24], edx
0046C35B  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
0046C35E  48 C1 EA 20                     shr rdx, 0x20
0046C362  44 0F B7 C2                     movzx r8d, dx
0046C366  41 C1 E0 06                     shl r8d, 6
0046C36A  41 8B D0                        mov edx, r8d
0046C36D  33 D0                           xor edx, eax
0046C36F  81 E2 3F 00 FF FF               and edx, 0xffff003f
0046C375  41 33 D0                        xor edx, r8d
0046C378  89 51 20                        mov dword ptr [rcx + 0x20], edx
0046C37B  C3                              ret
0046C37C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Mi4KStartForSubsection(__int64 a1, __int64 a2)
{
    *(unsigned int *)(a1 + 36) = (unsigned int)(a2);
    a2 = (a2) >> (32);
    a3 = (unsigned int)(((unsigned __int16)(a2)) << (6));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a3))) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))));
    a2 = (unsigned int)((a2) & (0xFFFF003FULL));
    a2 = (unsigned int)((a2) ^ ((unsigned int)(a3)));
    *(unsigned int *)(a1 + 32) = (unsigned int)(a2);
    return (unsigned int)(*(unsigned int *)(a1 + 32));
}
```

## 5. (Beta) C Style

```c
int64_t Mi4KStartForSubsection(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    *(uint32_t *)(arg1 + 0x24) = (uint32_t)(Arg2);
    Arg2 = (Arg2) >> (32);
    a3 = (uint32_t)(((uint16_t)(Arg2)) << (6));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(a3))) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))));
    Arg2 = (uint32_t)((Arg2) & (0xFFFF003FULL));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(a3)));
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)(Arg2);
    return (uint32_t)(*(uint32_t *)(arg1 + 0x20));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `W` |
| `Arg1` | `+ 0x24` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0046C358&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0046C358[BB_0046C358]
  bb_0046C37C[BB_0046C37C]
```
