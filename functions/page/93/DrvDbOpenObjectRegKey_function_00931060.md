# DrvDbOpenObjectRegKey

- RVA: `0x00931060`–`0x0093107C` (길이 `28` bytes)
- VA: `0x0000000140931060`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008EC64`
- 디코드: `10`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [DrvDbGetDriverDatabaseMappedPropertyKeys](../83/DrvDbGetDriverDatabaseMappedPropertyKeys_function_0083355C.md) at `0x0083366F`
- [DrvDbOpenDriverFileRegKey](../83/DrvDbOpenDriverFileRegKey_function_00833FCC.md) at `0x00834001`
- [DrvDbSetDriverDatabaseMappedProperty](../83/DrvDbSetDriverDatabaseMappedProperty_function_00834014.md) at `0x00834482`
- [DrvDbCreateDatabaseNode](../83/DrvDbCreateDatabaseNode_function_0083533C.md) at `0x008355E7`
- [DrvDbSetDeviceIdMappedProperty](../92/DrvDbSetDeviceIdMappedProperty_function_0092ECCC.md) at `0x0092EDB6`
- [DrvDbGetDriverDatabaseMappedProperty](../92/DrvDbGetDriverDatabaseMappedProperty_function_0092EE28.md) at `0x0092F062`
- [DrvDbOpenDeviceIdRegKey](../92/DrvDbOpenDeviceIdRegKey_function_0092F080.md) at `0x0092F0B5`
- [DrvDbGetDeviceIdMappedProperty](../92/DrvDbGetDeviceIdMappedProperty_function_0092F690.md) at `0x0092F7B5`
- [DrvDbGetDeviceIdMappedProperty](../92/DrvDbGetDeviceIdMappedProperty_function_0092F690.md) at `0x0092F9C1`
- [DrvDbGetObjectDatabaseNodeName](../92/DrvDbGetObjectDatabaseNodeName_function_0092FAC4.md) at `0x0092FB16`
- [DrvDbGetDriverInfFileMappedProperty](DrvDbGetDriverInfFileMappedProperty_function_00930080.md) at `0x00930140`
- [DrvDbOpenDriverInfFileRegKey](DrvDbOpenDriverInfFileRegKey_function_00930354.md) at `0x00930389`
- [DrvDbDispatchDriverPackage](DrvDbDispatchDriverPackage_function_009303A0.md) at `0x0093048C`
- [DrvDbGetDriverPackageMappedProperty](DrvDbGetDriverPackageMappedProperty_function_009305BC.md) at `0x0093073C`
- [DrvDbGetDriverPackageMappedProperty](DrvDbGetDriverPackageMappedProperty_function_009305BC.md) at `0x009308E3`
- [DrvDbOpenDriverPackageRegKey](DrvDbOpenDriverPackageRegKey_function_00931014.md) at `0x00931049`
- [sub_00B23888](../B2/Unknown_function_00B23888.md) at `0x00B23C26`
- [sub_00B23888](../B2/Unknown_function_00B23888.md) at `0x00B23CE3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00931060  48 8B C4                        mov rax, rsp
00931063  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00931067  48 89 48 08                     mov qword ptr [rax + 8], rcx
0093106B  55                              push rbp
0093106C  53                              push rbx
0093106D  56                              push rsi
0093106E  57                              push rdi
0093106F  41 55                           push r13
00931071  48 8D 68 C9                     lea rbp, [rax - 0x37]
00931075  48 81 EC 90 00 00 00            sub rsp, 0x90
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DrvDbOpenObjectRegKey(__int64 a1, __int64 a2, int a3)
{
    __int64 v_rsp;

    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (144);
    return v_rsp;
}
```

## 5. (Beta) C Style

```c
int64_t DrvDbOpenObjectRegKey(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t local_rsp;

    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (144);
    return local_rsp;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00931060&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00931060[BB_00931060]
```
